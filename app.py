import numpy as np
from flask import Flask,request,jsonify,render_template
from joblib import load
app=Flask(__name__)
model=load('admissionregress.save')


@app.route('/')
def home():
     return render_template('admission.html')


@app.route('/y_predict',methods=['POST'])
def y_predict():
       x_test=[[float(x) for x in request.form.values()]] 
       print(x_test)
       
       prediction=model.predict(x_test)
       print(prediction)
       output=prediction[0]
       return render_template('admission.html',prediction_text='Chance of Admission: {}'.format(output))  


if __name__ == "__main__":
         app.run(debug=True)     