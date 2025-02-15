Customer Churn Prediction Web App

																															 
This is a Flask-based web application for predicting customer churn. 
It loads a pre-trained machine learning model and provides predictions based on user inputs. 
The app takes various customer attributes as input and determines whether the customer is likely to churn or stay.



Features
Web-based UI using Flask and HTML templates.
Machine Learning Integration using a pre-trained model (lr_xg_model.sav).
User Input Handling: Accepts multiple customer attributes through an HTML form.
Binary Prediction Output: Displays whether a customer will churn or not.


Requirements
Ensure you have the following installed:
pip install flask pickle

project-directory
app.py                   # Main Flask application
lr_xg_model.sav          # Pre-trained ML model


templates/
index.html           # HTML template for UI

How It Works
The application loads the ML model from lr_xg_model.sav.
It provides an HTML form for users to input customer details.
When the user submits the form:
The input values are extracted and processed.
The model makes a prediction on whether the customer will churn.
The result is displayed on the web page.


Running the Application
Run the app with:
python app.py
By default, the Flask server runs on http://127.0.0.1:5000/

![Screenshot (281)](https://github.com/user-attachments/assets/2f969d1e-1041-472d-bf44-debf764f65a4)


![Screenshot (282)](https://github.com/user-attachments/assets/cd5affab-60dd-4433-b7ce-49ee95ef2ae9)



