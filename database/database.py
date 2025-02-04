import pymongo
import os
from config import DB_URI, DB_NAME

# Validate DB_URI
if not DB_URI:
    raise ValueError("Database URI is missing. Set DB_URI in config.py")

try:
    dbclient = pymongo.MongoClient(DB_URI)  # Connect to MongoDB
    database = dbclient[DB_NAME]  # Select database
    user_data = database["users"]  # Select collection
except pymongo.errors.ConnectionError as e:
    print(f"MongoDB Connection Error: {e}")
    exit(1)

async def present_user(user_id: int):
    """Check if user exists"""
    return bool(user_data.find_one({'_id': user_id}))

async def add_user(user_id: int):
    """Add a new user"""
    if not present_user(user_id):
        user_data.insert_one({'_id': user_id})

async def full_userbase():
    """Get list of all user IDs"""
    return [doc['_id'] for doc in user_data.find()]

async def del_user(user_id: int):
    """Delete a user"""
    user_data.delete_one({'_id': user_id})
