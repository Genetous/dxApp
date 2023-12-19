from pymongo import MongoClient
import datetime
import calendar
import pymongo
from bson.json_util import dumps
from bson.json_util import loads
import json
from bson.objectid import ObjectId
from bson.code import Code
class Mongo:
    def __init__(self, dbname):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client[dbname]
    def insertCollection(self, data):
        try:
            self.collection = self.db["collection"]
            val = self.collection.insert_one(data)
            return str(val.inserted_id)
        except:
            return None
    def insertRelation(self, data):
        try:
            self.relation = self.db["relation"]
            val = self.relation.insert_one(data)
            return str(val.inserted_id)
        except:
            return None