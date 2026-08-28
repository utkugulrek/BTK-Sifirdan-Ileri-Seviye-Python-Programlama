"""Kayıt güncelleme -> .update_one(), .update_many()"""

import pymongo

my_client = pymongo.MongoClient(
    "mongodb+srv://utkush2_db_user:{password}@cluster0.vwxvp3u.mongodb.net/?appName=Cluster0"
)

my_db = my_client["node-app"]
my_collection = my_db["products"]

# İlk {} filtreleme, ikinci {} güncelleme
my_collection.update_one(
    {"name": "Samsung S6"},
    {"$set":{
        "name": "iPhone 5S",
        "price": 5000
    }})

for i in my_collection.find():
    print(i)

####################################################################################################

# update_many() her eşleşeni değiştirir
my_collection.update_many(
    {"name": "Samsung S7"},
    {"$set":{
        "name": "iPhone 11",
        "price": 10000
    }})

for i in my_collection.find():
    print(i)

####################################################################################################

# Daha profesyonel yaklaşım
query = {"name": "Samsung S8"}
new_values = {"$set":{"name": "iPhone 11","price": 10000}}

result = my_collection.update_many(query, new_values)  # Kaç kayıt güncellendi

for i in my_collection.find():
    print(i)

print(f"{result.modified_count} adet kayıt güncellendi.")
