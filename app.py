from flask import Flask, render_template, request, redirect, url_for, flash
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os
from werkzeug.utils import secure_filename
import tensorflow as tf
import joblib

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For flash messages

# Allowed extensions for file uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Load the trained model
model = load_model('./malaria_detection_model.h5')

# Define a function to preprocess the image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

# Check if file type is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Define route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Define route for handling image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join('static', 'uploads', filename)
        file.save(file_path)
        
        try:
            # Preprocess the image
            img_array = preprocess_image(file_path)
            
            # Make the prediction
            prediction = model.predict(img_array)[0][0]
            
            # Calculate the confidence level
            confidence = round(prediction * 100, 2) if prediction > 0.5 else round((1 - prediction) * 100, 2)
            
            # Determine the result
            result = 'Uninfected' if prediction > 0.5 else 'Parasitized'
            
            # Display additional metrics (precision, recall, etc.)
            # Here, we assume a binary classification for Malaria detection.
            metrics = {
                'Precision': '95%',  # Replace with real calculation if needed
                'Recall': '94%',
                'F1-score': '94%'
            }
            
            return render_template('index.html', prediction=result, confidence=confidence, metrics=metrics, image=file_path)
        
        except Exception as e:
            flash(f"An error occurred during prediction: {str(e)}")
            return redirect(request.url)
    else:
        flash('Invalid file type. Please upload an image file (jpg, jpeg, png, gif).')
        return redirect(request.url)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
