import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

client = pymongo.MongoClient(os.getenv('MONGO_CONN'))
db = client[os.getenv('MONGO_DB')]