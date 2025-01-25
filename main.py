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
def get_records():
    # Check if we can connect to the database and fetch records
    records = db.records.find()  # Ensure this is the correct collection name
    
    # Log the number of records fetched for debugging
    print(f"Found {records.count()} records")  # Make sure you are using the correct count function
     
    # Return the data as JSON
    records_list = list(records)
    print(f"Records: {records_list}")  # Check the structure of the data

    return jsonify({"records": records_list})

# Example: Retrieve all records
@app.route('/records', methods=['GET'])
def get_records():
    records = db.records.find()  # Make sure you're using the correct collection name
    return jsonify({"records": list(records)})  # Convert cursor to a list

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Use 0.0.0.0 for Render compatibility
