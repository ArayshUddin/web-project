
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://araysh55:AUk0htoruDAXmmHS@araysh.2xsbb.mongodb.net/?retryWrites=true&w=majority&appName=araysh"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1')) 

db = client.todo.db
collection= db ["todo_data"]

