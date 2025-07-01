from flask import Flask, render_template,request
import requests

BACKEND_URL="http://127.0.0.1:9000"

app=Flask(__name__)

@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/submit",methods=['POST'])
def submit():
    form_data = dict(request.form)
    requests.post(BACKEND_URL+'/submit',json=form_data)
    return render_template("success.html")

@app.route("/view")
def view():
    #send an HTTP GET request to a BACKEND_URL and retrieve data from a web server/backend.
    response=requests.get(BACKEND_URL+'/view')
    return render_template("view.html",data=response.json())
    



if __name__=='__main__':
    app.run(port=8000,debug=True)