from pymongo.mongo_client import MongoClient
import datetime
uri="mongodb+srv://mukanbalasha:bala123@cluster0.o1iikds.mongodb.net/"
client=MongoClient(uri)
try:
    client.admin.command('ping')
    print("pinged your deployment.you successfully connected to mongoDB")
except Exception as e:
    print(e)