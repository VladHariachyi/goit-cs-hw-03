from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER_NAME = os.getenv("MONGO_DB_USER_NAME")
DB_USER_PASS = os.getenv("MONGO_DB_USER_PASS")

client = MongoClient(
    f"mongodb+srv://{DB_USER_NAME}:{DB_USER_PASS}@cluster0.pknxvtd.mongodb.net",
    server_api=ServerApi('1')
)

db = client.cats
