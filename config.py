from pymongo import MongoClient

DATABASE = MongoClient()['simplerestapi']
DEBUG = True
client = MongoClient('localhost',27017)