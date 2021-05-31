import pymongo
import urllib
from bson.objectid import ObjectId
from dotenv import dotenv_values

config = dotenv_values(".env")

def get_connection_string():
    return f'mongodb+srv://{config["MONGO_USER"]}:{urllib.parse.quote(config["MONGO_PASSWORD"])}@python2021.ftcmy.mongodb.net/{config["MONGO_DATABASE"]}?retryWrites=true&w=majority'

def connect():
    return pymongo.MongoClient(get_connection_string())


def disconnect(connection):
    connection.close()

def getAll(collection, query):
    connection = connect()
    db = connection[config["MONGO_DATABASE"]]
    response = db[collection].find(query)
    disconnect(connection)
    return response

def get(collection, id):
    connection = connect()
    db = connection[config["MONGO_DATABASE"]]
    response = db[collection].find_one({"_id": ObjectId(id)})
    disconnect(connection)
    return response

def create(collection, data):
    connection = connect()
    db = connection[config["MONGO_DATABASE"]]
    response = db[collection].insert_one(data)
    disconnect(connection)
    return response.inserted_id

def update(collection, id, data):
    connection = connect()
    db = connection[config["MONGO_DATABASE"]]
    response = db[collection].update_one({"_id": ObjectId(id)}, {"$set": data})
    disconnect(connection)
    return response.modified_count

def delete(collection, id):
    connection = connect()
    db = connection[config["MONGO_DATABASE"]]
    response = db[collection].delete_one({"_id": ObjectId(id)})
    disconnect(connection)
    return response.deleted_count

if __name__ == "__main__":
    #inserted_id = create("users", {"name": "Tania"})
    #user = get("users", inserted_id)
    user = get("users", "60b47392036429b66b7b431b")
    print(user)
