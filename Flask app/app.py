from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient

load_dotenv()

MONGO_URI = os.getenv('uri')

#creates a connection to a MongoDB database.
client = MongoClient(MONGO_URI)

#selects (or creates, if it doesn’t already exist) a database
db=client.test

#Create a collection named flask-tutorial || access a collection
collection = db['flask-tutorial']

app=Flask(__name__)

@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/submit",methods=['POST'])
def submit():  
    form_data=dict(request.form)
    #insert form data to Mongodb collection
    collection.insert_one(form_data)
    return "Account Created successfully"

@app.route("/view")
def view():
    #fetching data from mongodb
    all_data=list(collection.find())
    
    return render_template("view.html",data=all_data)



if __name__=='__main__':
    app.run(debug=True)