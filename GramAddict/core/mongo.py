from os import getenv

from pymongo import MongoClient

client = MongoClient(getenv("MONGO_URI" "mongodb://localhost:27017/"))
mongo = client.gramaddict

print(f"Count interacted users = {mongo.interacted_users.count_documents({})}")
