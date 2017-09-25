import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://garciaryan:4cC6^UdYKt@ds149724.mlab.com:49724/nba-stats')

db = client['nba-data']

print('it ran!')