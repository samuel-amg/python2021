import os

import pymongo
import urllib
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()

def get_connection_string():
    return f'mongodb+srv://{os.getenv("MONGO_USER")}:{urllib.parse.quote(os.getenv("MONGO_PASSWORD"))}@python2021.ftcmy.mongodb.net/{os.getenv("MONGO_DATABASE")}?retryWrites=true&w=majority'

def connect():
    return pymongo.MongoClient(get_connection_string())


def disconnect(connection):
    connection.close()

def getAll(collection, query):
    connection = connect()
    db = connection[os.getenv("MONGO_DATABASE")]
    response = list(db[collection].find(query))
    disconnect(connection)
    return response

def get(collection, id):
    connection = connect()
    db = connection[os.getenv("MONGO_DATABASE")]
    response = db[collection].find_one({"_id": ObjectId(id)})
    disconnect(connection)
    return response

def create(collection, data):
    connection = connect()
    db = connection[os.getenv("MONGO_DATABASE")]
    response = db[collection].insert_one(data)
    disconnect(connection)
    return response.inserted_id

def update(collection, id, data):
    connection = connect()
    db = connection[os.getenv("MONGO_DATABASE")]
    response = db[collection].update_one({"_id": ObjectId(id)}, {"$set": data})
    disconnect(connection)
    return response.modified_count

def delete(collection, id):
    connection = connect()
    db = connection[os.getenv("MONGO_DATABASE")]
    response = db[collection].delete_one({"_id": ObjectId(id)})
    disconnect(connection)
    return response.deleted_count
