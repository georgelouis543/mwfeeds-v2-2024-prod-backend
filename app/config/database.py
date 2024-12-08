from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGO_CLIENT_URI")
client = MongoClient(uri)


db = client.mwfeeds_staging_db

feed_collection = db["feed_collection"]
user_collection = db["user_collection"]
tag_collection = db["tag_collection"]
feed_content_collection = db["feed_content_collection"]
feed_params_collection = db["feed_params_collection"]
newsfeed_collection = db["newsfeed_collection"]
merged_feed_collection = db["merged_feed_collection"]
deleted_feed_collection = db["deleted_feed_collection"]
other_functions_collection = db["other_functions_collection"]