__author__='akishan'

import pymongo

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None
   
    @staticmethod    
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['bmi']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data) #data is JSON

    @staticmethod
    def find(collection,query):
        return Database.DATABASE[colection].find(query)

    @staticmethod
    def find_one(collection,query):
        return Database.DATABASE[collection].find_one(query)


