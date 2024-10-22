# malaria_ML
Malaria Detection Using Convolutional Neural Networks (CNNs)
This project is a Flask web application that detects whether a blood cell image is infected with malaria using a trained Convolutional Neural Network (CNN) model. The model processes the input image and provides a prediction along with confidence levels, making it easier to diagnose malaria in a non-invasive, quick manner.

Table of Contents
Overview
Features
Technologies Used
Installation
Usage
Model Training
Contributing
License
Overview
This project aims to assist medical professionals by providing a quick and reliable method to detect malaria in blood cell images. Using a Convolutional Neural Network, this application analyzes uploaded images to determine if the blood cells are parasitized or uninfected. The application also provides performance metrics (precision, recall, and F1-score) to demonstrate the model's effectiveness.

Features
Upload blood cell images in formats such as JPG, JPEG, PNG, or GIF.
Analyze the image for malaria infection.
Provides confidence level (%) for the prediction.
Displays model performance metrics (precision, recall, F1-score).
Clean, modern user interface built with Bootstrap.
Responsive design for both desktop and mobile usage.
Technologies Used
Frontend:

HTML5, CSS3 (Bootstrap 5)
JavaScript (for enhanced UI)
Backend:

Flask (Python)
Jinja2 templating engine
Machine Learning:

TensorFlow / Keras for model training and prediction.
Preprocessing with numpy and PIL for image handling.
Installation
1. Clone the repository
bash
Copy code
git clone https://github.com/barrack81/malaria_ML.git
cd malaria_ML
2. Create a Virtual Environment
It’s recommended to use a virtual environment to manage dependencies. Run the following commands:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
Install all required Python packages using the requirements.txt file.

bash
Copy code
pip install -r requirements.txt
4. Download or Place the Trained Model
Ensure the trained malaria detection model is saved as malaria_detection_model.h5 and place it in the project root directory.

5. Running the Application
Once everything is set up, start the Flask application:

bash
Copy code
flask run
The app will be available at http://127.0.0.1:5000.

Usage
Navigate to the homepage where you will see a file upload form.
Click on the Choose File button to upload a blood cell image.
Click Analyze Image to process the image.
After a few seconds, the app will display:
Whether the cell is Parasitized or Uninfected.
Confidence level (%) for the prediction.
Model performance metrics (precision, recall, F1-score).
A preview of the uploaded image for verification.
Example
If the prediction is Uninfected, it will show the result along with a confidence score like 95%.
Model metrics will include values like Precision: 95%, Recall: 94%, and F1-score: 94%.
Model Training
The trained model malaria_detection_model.h5 is created using a CNN architecture in Keras, with images from the Malaria Cell Image Dataset. The model is trained to classify cell images as either Parasitized or Uninfected. If you want to retrain the model or modify it, you can find the training notebook and dataset linked below:

Dataset: Malaria Cell Images Dataset
Model Training Notebook: Training Notebook
Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create your feature branch: git checkout -b feature/YourFeature.
Commit your changes: git commit -m 'Add your feature'.
Push to the branch: git push origin feature/YourFeature.
Submit a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.