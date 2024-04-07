from pymongo import MongoClient
from os import getenv
import certifi
from dotenv import load_dotenv

load_dotenv()

host_db = getenv("MONGO_HOST")
port_db = getenv("MONGO_PORT")
user_db = getenv("MONGO_USER")
password_db = getenv("MONGO_PASSWORD")

url = f"mongodb://{user_db}:{password_db}@{host_db}:{port_db}"

conn = MongoClient(url)
conn.database = conn.users
