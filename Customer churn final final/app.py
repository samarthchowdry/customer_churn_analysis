from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('lr_xg_model.sav', 'rb'))

@app.route('/')
def home():

  result = ''
  return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])

def predict():
  
  SeniorCitizen = int(request.form['SeniorCitizen'])
  tenure = int(request.form['tenure'])
  MonthlyCharges = float(request.form['MonthlyCharges'])
  TotalCharges = float(request.form['TotalCharges'])
  
  # Partner_Yes =request.form['Partner_Yes'].lower() == 'true'
  Partner =request.form['Partner']
  if Partner.lower() == 'yes':
    Partner_Yes=True
  
  else:
    Partner_Yes=False
    
 

  # gender_Male =request.form['gender_Male'].lower() == 'true'
  gender =request.form['gender']
  if gender.lower() == 'm':
    gender_Male=True
  
  else:
    gender_Male=False
    
    
  # Dependents_Yes =request.form['Dependents_Yes'].lower() == 'true'
  Dependents =request.form['Dependents']
  if Dependents.lower() == 'yes':
    Dependents_Yes=True
  
  else:
    Dependents_Yes=False
    
  
  
  # PhoneService_Yes =(request.form['PhoneService_Yes']).lower() == 'true'
  PhoneService =request.form['PhoneService']
  if PhoneService.lower() == 'yes':
    PhoneService_Yes=True
  
  else:
    PhoneService_Yes=False
  
  # MultipleLines_Nophoneservice =request.form['MultipleLines_No phone service'].lower() == 'true'
  # MultipleLines_Yes =request.form['MultipleLines_Yes'].lower() == 'true'
  MultipleLines =request.form['MultipleLines']
  if MultipleLines.lower() == 'no phone service':
    MultipleLines_Nophoneservice=True
    MultipleLines_Yes=False
  
  else:
    MultipleLines_Nophoneservice=False
    MultipleLines_Yes=True
  
  
  # InternetService_Fiberoptic =request.form['InternetService_Fiber optic'].lower() == 'true'
  # InternetService_No =request.form['InternetService_No'].lower() == 'true'
  InternetService =request.form['InternetService']
  if InternetService.lower() == 'fiber optic':
    InternetService_Fiberoptic=True
    InternetService_No=False
  
  elif InternetService.lower() == 'no':
    InternetService_Fiberoptic=False
    InternetService_No=True
  
  else:
    InternetService_Fiberoptic=False
    InternetService_No=False
    
  
  
  
  # OnlineSecurity_Nointernetservice=request.form['OnlineSecurity_No internet service'].lower() == 'true'
  # OnlineSecurity_Yes=request.form['OnlineSecurity_Yes'].lower() == 'true'
  OnlineSecurity =request.form['OnlineSecurity']
  if OnlineSecurity.lower() == 'no internet service':
    OnlineSecurity_Nointernetservice=True
    OnlineSecurity_Yes=False
  
  else:
    OnlineSecurity_Nointernetservice=False
    OnlineSecurity_Yes=True
  
  
  
  # OnlineBackup_Nointernetservice =request.form['OnlineBackup_No internet service'].lower() == 'true'
  # OnlineBackup_Yes =request.form['OnlineBackup_Yes'].lower() == 'true'
  OnlineBackup =request.form['OnlineBackup']
  if OnlineBackup.lower() == 'no internet service':
    OnlineBackup_Nointernetservice=True
    OnlineBackup_Yes=False
  
  else:
    OnlineBackup_Nointernetservice=False
    OnlineBackup_Yes=True
  
  
  # DeviceProtection_Nointernetservice=request.form['DeviceProtection_No internet service'].lower() == 'true'
  # DeviceProtection_Yes=request.form['DeviceProtection_Yes'].lower() == 'true'
  DeviceProtection =request.form['DeviceProtection']
  if DeviceProtection.lower() == 'no internet service':
    DeviceProtection_Nointernetservice=True
    DeviceProtection_Yes=False
  
  else:
    DeviceProtection_Nointernetservice=False
    DeviceProtection_Yes=True
  
  
  # TechSupport_Nointernetservice =request.form['TechSupport_No internet service'].lower() == 'true'
  # TechSupport_Yes=request.form['TechSupport_Yes'].lower() == 'true'
  TechSupport =request.form['TechSupport']
  if TechSupport.lower() == 'no internet service':
    TechSupport_Nointernetservice=True
    TechSupport_Yes=False
  
  else:
    TechSupport_Nointernetservice=False
    TechSupport_Yes=True
  
  
  # StreamingTV_Nointernetservice  =request.form['StreamingTV_No internet service'].lower() == 'true'
  # StreamingTV_Yes=request.form['StreamingTV_Yes'].lower() == 'true'
  StreamingTV =request.form['StreamingTV']
  if StreamingTV.lower() == 'no internet service':
    StreamingTV_Nointernetservice=True
    StreamingTV_Yes=False
  
  else:
    StreamingTV_Nointernetservice=False
    StreamingTV_Yes=True
  
  
  # StreamingMovies_Nointernetservice  =request.form['StreamingMovies_No internet service'].lower() == 'true'
  # StreamingMovies_Yes  =request.form['StreamingMovies_Yes'].lower() == 'true'
  StreamingMovies =request.form['StreamingMovies']
  if StreamingMovies.lower() == 'no internet service':
    StreamingMovies_Nointernetservice=True
    StreamingMovies_Yes=False
  
  else:
    StreamingMovies_Nointernetservice=False
    StreamingMovies_Yes=True
  
  
  # Contract_Oneyear =request.form['Contract_One year'].lower() == 'true'
  # Contract_Twoyear =request.form['Contract_Two year'].lower() == 'true'
  Contract =request.form['Contract']
  if Contract.lower() == 'one year':
    Contract_Oneyear=True
    Contract_Twoyear=False
  
  elif Contract.lower() == 'two year':
    Contract_Oneyear=False
    Contract_Twoyear=True
  else:
    Contract_Oneyear=False
    Contract_Twoyear=False
    
  
  
  # PaperlessBilling_Yes =request.form['PaperlessBilling_Yes'].lower() == 'true'
  PaperlessBilling =request.form['PaperlessBilling']
  if PaperlessBilling.lower() == 'yes':
    PaperlessBilling_Yes=True
  
  else:
    PaperlessBilling_Yes=False
  
  # PaymentMethod_Creditcard =request.form['PaymentMethod_Credit card (automatic)'].lower() == 'true'
  # PaymentMethod_Electroniccheck =request.form['PaymentMethod_Electronic check'].lower() == 'true'
  # PaymentMethod_Mailedcheck =request.form['PaymentMethod_Mailed check'].lower() == 'true'
  PaymentMethod =request.form['PaymentMethod']
  if PaymentMethod.lower() == 'credit card':
    PaymentMethod_Creditcard=True
    PaymentMethod_Electroniccheck=False
    PaymentMethod_Mailedcheck=False
  
  elif PaymentMethod.lower() == 'electronic card':
    PaymentMethod_Creditcard=False
    PaymentMethod_Electroniccheck=True
    PaymentMethod_Mailedcheck=False
  
  else:
    PaymentMethod_Creditcard=False
    PaymentMethod_Electroniccheck=False
    PaymentMethod_Mailedcheck=True
    
    
  result = model.predict([[SeniorCitizen,tenure,MonthlyCharges,TotalCharges,gender_Male,Partner_Yes,Dependents_Yes,PhoneService_Yes,MultipleLines_Nophoneservice,MultipleLines_Yes,InternetService_Fiberoptic,InternetService_No,OnlineSecurity_Nointernetservice,OnlineSecurity_Yes,OnlineBackup_Nointernetservice,OnlineBackup_Yes,DeviceProtection_Nointernetservice,DeviceProtection_Yes,TechSupport_Nointernetservice,TechSupport_Yes,StreamingTV_Nointernetservice ,StreamingTV_Yes,StreamingMovies_Nointernetservice,StreamingMovies_Yes,Contract_Oneyear,Contract_Twoyear,PaperlessBilling_Yes,PaymentMethod_Creditcard,PaymentMethod_Electroniccheck,PaymentMethod_Mailedcheck]])[0]
  if result==False:
      ans="Customer WILL NOT CHURN"

  else:
      ans="Customer WILL CHURN"

    
  return render_template('index.html', **locals())

if __name__ == '__main__':
  app.run(debug=True)