"""Kayıt silme -> .delete_one(), .delete_many()"""

import pymongo

my_client = pymongo.MongoClient(
    "mongodb+srv://utkush2_db_user:{password}@cluster0.vwxvp3u.mongodb.net/?appName=Cluster0"
)

my_db = my_client["node-app"]
my_collection = my_db["products"]

for i in my_collection.find():
    print(i)

print("*" * 100)

# {parametre}
my_collection.delete_one({"name": "Samsung S9"})

for i in my_collection.find():
    print(i)

print("*" * 100)

####################################################################################################

# .delete_many() eşleşen her kaydı siler
my_collection.delete_many({"name": {"$regex": "^i"}})

for i in my_collection.find():
    print(i)

result = my_collection.delete_many({})  # Tüm kayıtları siler
print(f"{result.deleted_count} tane kayıt silindi.")
