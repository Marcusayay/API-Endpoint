from flask import Flask, jsonify, request
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


# MongoDB connection
MONGODB_URI = os.getenv("MONGODB_URI")  # Get MongoDB URI from environment variable
client = MongoClient(MONGODB_URI)
db = client["Database_Name"]["Infected_Devices"]


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Python backend!"})

# Example: Create a new record in MongoDB
@app.route('/add', methods=['POST'])
def add_record():
    data = request.json
    db.example_collection.insert_one(data)
    return jsonify({"message": "Record added!", "data": data})


@app.route('/records', methods=['GET'])
def get_records():
    records = db.find()  # Retrieve all records from the correct collection
    records_list = []
    for record in records:
        record["_id"] = str(record["_id"])  # Convert ObjectId to string
        records_list.append(record)
    return jsonify({"records": records_list})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9000)  # Use 0.0.0.0 for Render compatibility
