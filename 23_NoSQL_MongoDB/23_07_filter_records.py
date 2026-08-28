"""Kayıt getirirken filtrelemek"""

from bson.objectid import ObjectId  # id ile sorgu için gerekli
import pymongo

my_client = pymongo.MongoClient(
    "mongodb+srv://utkush2_db_user:{password}@cluster0.vwxvp3u.mongodb.net/?appName=Cluster0"
)

my_db = my_client["node-app"]
my_collection = my_db["products"]

my_filter = {"name": "Samsung S5"}

result = my_collection.find(my_filter)

for r in result:
    print(r)

####################################################################################################

# id için ObjectId gerekiyor
result = my_collection.find_one({"_id": ObjectId("6a918e3a57d297865119f9df")})

print(result)

####################################################################################################

result = my_collection.find(
    {"name": {"$in": ["Samsung S5", "Samsung S6"]}}  # $eq, eşittir equal
)

for r in result:
    print(r)

####################################################################################################

# MongoDB Operators
result = my_collection.find(
    {"price": {"$gt": 2000}}  # gt -> greater than, gte -> gt + equal, lt -> less than
)

for r in result:
    print(r)

####################################################################################################

# Regex
result = my_collection.find({"name": {"$regex": "^S"}})

for r in result:
    print(r)
