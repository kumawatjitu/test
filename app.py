import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
#from flask_ngrok import run_with_ngrok
import pickle
#from jinja2 import Template

app = Flask(__name__)

#run_with_ngrok(app)

@app.route('/')
def index():
  
    return render_template("index.html")
#------------------------------About us-------------------------------------------
@app.route('/aboutus')
def aboutus():
    
    return render_template('aboutus.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



@app.route('/internship',methods=['GET'])
def internship():
    return render_template('internship.html')


@app.route('/login',methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/register',methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/SVM',methods=['GET'])
def SVM():

    return render_template('SVM.html')
@app.route('/Decision',methods=['GET'])
def Decision():
 
    return render_template('Decision.html')
@app.route('/KNN',methods=['GET'])
def KNN():
    return render_template('KNN.html')

@app.route('/Random',methods=['GET'])
def Random():
    return render_template('Random.html')

@app.route('/Naive',methods=['GET'])
def Naive():
    return render_template('Naive.html')

@app.route('/Logestic',methods=['GET'])
def Logistic():
    return render_template('Logistic.html')

@app.route('/mini',methods=['GET'])
def mini():
    return render_template('mini.html')




@app.route('/predict',methods=['GET'])
def predict():
    
    wth=float(request.args.get('wth'))
    tenure=float(request.args.get('tenure'))
    hsa=float(request.args.get('hsa'))
    ndr=float(request.args.get('ndr'))
    sfs=float(request.args.get('sfs'))
    noa=float(request.args.get('noa'))
    oahl = float(request.args.get('oahl'))
    cu=float(request.args.get('cu'))
    oc=float(request.args.get('oc'))
    dslo=float(request.args.get('dslo'))
    ca=float(request.args.get('ca'))
    City=float(request.args.get('City'))
    gender=float(request.args.get('gender'))
    pld=float(request.args.get('pld'))
    complain=float(request.args.get('complain'))
    Status=float(request.args.get('Status'))
    ppm=float(request.args.get('ppm'))
    poc=float(request.args.get('poc'))
    
    model=pickle.load(open('decision_model_major.pkl', 'rb'))
    
    

    prediction = model.predict([[wth,tenure,hsa,ndr,sfs,noa,oahl,cu,oc,dslo,ca,City,gender,pld,complain,Status,ppm,poc]])
    if prediction==0:
      message="Customer will Buy Again"
    else:
      message="Customer will Not Buy Again"
    
        
    return render_template('predict.html', prediction_text='Model  has predicted : {}'.format(message))

@app.route('/predict1',methods=['GET'])
def predict1():
    tenure = float(request.args.get('tenure'))
    wth=float(request.args.get('wth'))
    hsa=float(request.args.get('hsa'))
    ndr=float(request.args.get('ndr'))
    sfs=float(request.args.get('sfs'))
    noa=float(request.args.get('noa'))
    oahl = float(request.args.get('oahl'))
    cu=float(request.args.get('cu'))
    oc=float(request.args.get('oc'))
    dslo=float(request.args.get('dslo'))
    ca=float(request.args.get('ca'))
    City=float(request.args.get('City'))
    gender=float(request.args.get('gender'))
    pld=float(request.args.get('pld'))
    complain=float(request.args.get('complain'))
    Status=float(request.args.get('Status'))
    ppm=float(request.args.get('ppm'))
    poc=float(request.args.get('poc'))
 


    model=pickle.load(open('svm_major.pkl','rb'))
    
    prediction = model.predict([[tenure,wth,hsa,ndr,sfs,noa,oahl,cu,oc,dslo,ca,City,gender,pld,complain,Status,ppm,poc]])
       
           
    if prediction==0:
        message="Customer will not Buy Again"
    else:
        message="Customer will Buy Again"
    
        
    return render_template('predict.html', prediction_text='Model  has predicted : {}'.format(message))


@app.route('/predict2',methods=['GET'])
def predict2():
    tenure = float(request.args.get('tenure'))
    wth=float(request.args.get('wth'))
    hsa=float(request.args.get('hsa'))
    ndr=float(request.args.get('ndr'))
    sfs=float(request.args.get('sfs'))
    noa=float(request.args.get('noa'))
    oahl = float(request.args.get('oahl'))
    cu=float(request.args.get('cu'))
    oc=float(request.args.get('oc'))
    dslo=float(request.args.get('dslo'))
    ca=float(request.args.get('ca'))
    City=float(request.args.get('City'))
    gender=float(request.args.get('gender'))
    pld=float(request.args.get('pld'))
    complain=float(request.args.get('complain'))
    Status=float(request.args.get('Status'))
    ppm=float(request.args.get('ppm'))
    poc=float(request.args.get('poc'))
    
    model=pickle.load(open('knn_major.pkl','rb'))
  
    prediction = model.predict([[tenure,wth,hsa,ndr,sfs,noa,oahl,cu,oc,dslo,ca,City,gender,pld,complain,Status,ppm,poc]])
     
         
    if prediction==0:
      message="Customer will not Buy Again"
    else:
      message="Customer will Buy Again"
    
        
    return render_template('predict.html', prediction_text='Model  has predicted : {}'.format(message))



@app.route('/predict3',methods=['GET'])
def predict3():
    tenure = float(request.args.get('tenure'))
    wth=float(request.args.get('wth'))
    hsa=float(request.args.get('hsa'))
    ndr=float(request.args.get('ndr'))
    sfs=float(request.args.get('sfs'))
    noa=float(request.args.get('noa'))
    oahl = float(request.args.get('oahl'))
    cu=float(request.args.get('cu'))
    oc=float(request.args.get('oc'))
    dslo=float(request.args.get('dslo'))
    ca=float(request.args.get('ca'))
    City=float(request.args.get('City'))
    gender=float(request.args.get('gender'))
    pld=float(request.args.get('pld'))
    complain=float(request.args.get('complain'))
    Status=float(request.args.get('Status'))
    ppm=float(request.args.get('ppm'))
    poc=float(request.args.get('poc'))
   


    model=pickle.load(open('random_forest_major.pkl','rb'))

    prediction = model.predict([[tenure,wth,hsa,ndr,sfs,noa,oahl,cu,oc,dslo,ca,City,gender,pld,complain,Status,ppm,poc]])
       
           
    if prediction==0:
        message="Customer will not Buy Again"
    else:
        message="Customer will Buy Again"
    
        
    return render_template('predict.html', prediction_text='Model  has predicted : {}'.format(message))


@app.route('/predict4',methods=['GET'])
def predict4():
    
    tenure = float(request.args.get('tenure'))
    wth=float(request.args.get('wth'))
    hsa=float(request.args.get('hsa'))
    ndr=float(request.args.get('ndr'))
    sfs=float(request.args.get('sfs'))
    noa=float(request.args.get('noa'))
    oahl = float(request.args.get('oahl'))
    cu=float(request.args.get('cu'))
    oc=float(request.args.get('oc'))
    dslo=float(request.args.get('dslo'))
    ca=float(request.args.get('ca'))
    City=float(request.args.get('City'))
    gender=float(request.args.get('gender'))
    pld=float(request.args.get('pld'))
    complain=float(request.args.get('complain'))
    Status=float(request.args.get('Status'))
    ppm=float(request.args.get('ppm'))
    poc=float(request.args.get('poc'))
  

    model=pickle.load(open('naive_major.pkl','rb'))

    prediction = model.predict([[tenure,wth,hsa,ndr,sfs,noa,oahl,cu,oc,dslo,ca,City,gender,pld,complain,Status,ppm,poc]])
       
           
    if prediction==0:
        message="Customer will not Buy Again"
    else:
        message="Customer will Buy Again"
    return render_template('predict.html', prediction_text='Model  has predicted : {}'.format(message))
      
      
@app.route('/predict5',methods=['GET'])
def predict5():
    tenure = float(request.args.get('tenure'))
    wth=float(request.args.get('wth'))
    hsa=float(request.args.get('hsa'))
    ndr=float(request.args.get('ndr'))
    sfs=float(request.args.get('sfs'))
    noa=float(request.args.get('noa'))
    oahl = float(request.args.get('oahl'))
    cu=float(request.args.get('cu'))
    oc=float(request.args.get('oc'))
    dslo=float(request.args.get('dslo'))
    ca=float(request.args.get('ca'))
    City=float(request.args.get('City'))
    gender=float(request.args.get('gender'))
    pld=float(request.args.get('pld'))
    complain=float(request.args.get('complain'))
    Status=float(request.args.get('Status'))
    ppm=float(request.args.get('ppm'))
    poc=float(request.args.get('poc'))
  

    model=pickle.load(open('log_reg.pkl','rb'))

    prediction = model.predict([[tenure,wth,hsa,ndr,sfs,noa,oahl,cu,oc,dslo,ca,City,gender,pld,complain,Status,ppm,poc]])
       
           
    if prediction==0:
        message="Customer will not Buy Again"
    else:
        message="Customer will Buy Again"
    
        
    return render_template('predict.html', prediction_text='Model  has predicted : {}'.format(message))



if __name__ == "__main__":
  app.run()

