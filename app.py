import flask
import pandas as pd
from flask import Flask,render_template,request
from sklearn.linear_model import LinearRegression
import pickle
with open("mul_lin_reg.pkl","rb") as r:
    m=pickle.load(r)

app=Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")
@app.route("/predict",methods=["GET","POST"])
def predict():

    l = list(request.form.values())
    a = [float(i) for i in l[1:]]
    date = pd.to_datetime(l[0], dayfirst=False, errors='coerce')
    a.append(date.day)
    a.append(date.month)
    a.append(date.year)
    s = m.predict([a])
    return render_template('index.html', result=float(s[0]))
if __name__=="__main__":
    app.run(debug=True)