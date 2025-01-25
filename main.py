from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
MONGODB_URI = os.getenv("MONGODB_URI")  # Get MongoDB URI from environment variable
client = MongoClient(MONGODB_URI)
db = client["Infected_Devices"]  # Replace with your database name

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Python backend!"})

# Example: Create a new record in MongoDB
@app.route('/add', methods=['POST'])
def add_record():
    data = request.json
    db.example_collection.insert_one(data)
    return jsonify({"message": "Record added!", "data": data})

# Example: Retrieve all records
@app.route('/records', methods=['GET'])
def get_records():
    records = list(db.example_collection.find({}, {"_id": 0}))  # Exclude MongoDB's ObjectId
    return jsonify({"records": records})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Use 0.0.0.0 for Render compatibility
