__author__ = "rmaynars"

import pymongo

uri = "mongodb://127.0.0.1:27017"

client = pymongo.MongoClient(uri)
database = client['udemy']
collection = database['students']

students = [print(student) for student in collection.find({}) if student['age'] > 30]

