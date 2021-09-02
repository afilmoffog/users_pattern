import os

from dotenv import load_dotenv
import motor.motor_asyncio
from fastapi_users.db import MongoDBUserDatabase

from users_pattern.models.user import UserDB

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_URI"), uuidRepresentation="standard")
db = client.onlycunts

user_collection = db["users"]
user_db = MongoDBUserDatabase(UserDB, user_collection)



