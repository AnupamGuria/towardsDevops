from flask import Flask,render_template,request
import requests

BACKEND_URL ="http://127.0.0.1:8000"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submittodoitem",methods=['POST'])
def submit():
    form_data=dict(request.form)
    requests.post(BACKEND_URL+'/submittodoitem',json=form_data)
    return "data submitted"

if __name__ == '__main__':
    app.run(port=3000, debug=True)

