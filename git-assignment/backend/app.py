from flask import Flask,request
from dotenv import load_dotenv
import os

from pymongo.mongo_client import MongoClient

load_dotenv()
MONGO_URI=os.getenv('uri')
client =MongoClient(MONGO_URI)

db=client.item
collection = db['github']

app = Flask(__name__)

@app.route("/submittodoitem",methods=['post'])
def submit():
    form_data=request.json
    collection.insert_one(form_data)
    return "submit"

if __name__ == '__main__':
    app.run(port=8000, debug=True)

