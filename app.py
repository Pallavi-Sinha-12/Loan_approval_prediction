# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('loan_approval.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
  if request.method == 'POST':
    # Gender
    sex = request.form['Gender']
    if (sex == 'Male'):
      Gender = 1

    else:
      Gender = 0
    Married = request.form["Married"]
    if (Married== 'Yes'):
      Married = 1
    else:
      Married = 0
    nod = request.form["Number of dependents"]
    if nod == 0:
      Dependents_0 = 1
      Dependents_1 = 0
      Dependents_2 = 0
      Dependents_3 = 0
    elif nod==1:
      Dependents_0 = 0
      Dependents_1 = 1
      Dependents_2 = 0
      Dependents_3 = 0
    elif nod == 2:
      Dependents_0 = 0
      Dependents_1 = 0
      Dependents_2 = 1
      Dependents_3 = 0
    else:
      Dependents_0 = 0
      Dependents_1 = 0
      Dependents_2 = 0
      Dependents_3 = 1
    emp = request.form["Self_Employed"]
    if emp == "Yes":
      Self_Employed = 1
    else:
      Self_Employed = 0
    edu = request.form["Education"]
    if edu == "Graduate":
      Education = 0
    else:
      Education = 1
    lat = request.form["Loan_Amount_Term"]
    Loan_Amount_Term = lat
    his = request.form["Credit_History"]
    Credit_History = his
    area = request.form["Property_Area"]
    if area == "Urban":
      Property_Area_Rural = 0
      Property_Area_Urban = 1
      Property_Area_Semiurban = 0
    elif area == "Rural":
      Property_Area_Rural = 1
      Property_Area_Urban = 0
      Property_Area_Semiurban = 0
    else:
      Property_Area_Rural = 0
      Property_Area_Urban = 0
      Property_Area_Semiurban = 1
    ApplicantIncome = request.form["ApplicantIncome"]
    CoapplicantIncome = request.form["CoapplicantIncome"]
    LoanAmount = request.form["LoanAmount"]
    prediction = model.predict([[
      Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount,
      Loan_Amount_Term, Credit_History, Dependents_0, Dependents_1, Dependents_2,
      Dependents_3, Property_Area_Rural,  Property_Area_Semiurban,Property_Area_Urban
    ]])
    if prediction==0:
      return render_template('index.html',prediction_text="Sorry your loan cannot be approved.")
    else:
      return render_template('index.html',prediction_text="Congratulations! your loan can be approved.")

if __name__ == '__main__':
	app.run(debug=True)