from flask import Flask, request, jsonify
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

@app.route("/submit",methods=['POST'])
def submit():  
    form_data=dict(request.json)
    #insert form data to Mongodb collection
    collection.insert_one(form_data)
    return "Account Created successfully"

@app.route("/view")
def view():
    #fetching data from mongodb
    all_data=list(collection.find())
    for item in all_data:
        del(item['_id'])
    #data={'data':all_data}
    return jsonify(all_data)
    



if __name__=='__main__':
    app.run(port=9000,debug=True)