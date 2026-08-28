"""Kayıt getirirken sıralama -> .sort()"""

import pymongo

my_client = pymongo.MongoClient(
    "mongodb+srv://utkush2_db_user:{password}@cluster0.vwxvp3u.mongodb.net/?appName=Cluster0"
)

my_db = my_client["node-app"]
my_collection = my_db["products"]

result = my_collection.find().sort("name")  # Alfabetik
result = my_collection.find().sort("name", -1)  # Tersten

result = my_collection.find().sort("price")  # Azdan çoka
result = my_collection.find().sort("price", -1)  # Çoktan aza

result = my_collection.find().sort([("name",1), ("price", -1)])  # Fazla kriterli sıralama

for r in result:
    print(r)
