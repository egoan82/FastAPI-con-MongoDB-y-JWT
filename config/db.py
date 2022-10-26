from pymongo import MongoClient
from os import getenv
import certifi
from dotenv import load_dotenv

load_dotenv()

url = "mongodb+srv://%s:%s@cluster0.m8gyh.mongodb.net/?retryWrites=true&w=majority" % (
    getenv("MONGO_USER"),
    getenv("MONGO_PASSWORD")
)

conn = MongoClient(url, tlsCAFile=certifi.where())
