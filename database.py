import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['udemy']

    @staticmethod
    def insert(collection, query):
        Database.DATABASE[collection].insert(query)

    @staticmethod
    def find(collection, query):
        Database.DATABASE[collection].find(query)\

    @staticmethod
    def findOne(collection, query):
        Database.DATABASE[collection].find_one(query)

