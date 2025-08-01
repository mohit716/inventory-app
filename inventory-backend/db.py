# db.py
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
_client = MongoClient(MONGO_URI)              # singleton client
_db = _client["inventory"]

def get_items_collection():
    return _db["items"]
