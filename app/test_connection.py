from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi  # Import certifi for CA bundle

# Load environment variables
load_dotenv()

# Retrieve the database URL
db_url = os.getenv("DB_URL")

try:
    # Connect to MongoDB with the CA file
    client = MongoClient(db_url, tlsCAFile=certifi.where())
    print("Connected to MongoDB!")
    print("Databases:", client.list_database_names())
except Exception as e:
    print("Connection Failed:", str(e))
