from pymongo import MongoClient
from pymongo.server_api import ServerApi


client = MongoClient(
    "",
    server_api=ServerApi('1')
)

db = client.test



class Api:
    def __init__(self):
        pass

