"""Collections oluşturma -> .insert_one(), .insert_many()"""

import pymongo

my_client = pymongo.MongoClient(
    "mongodb+srv://utkush2_db_user:{password}@cluster0.vwxvp3u.mongodb.net/?appName=Cluster0"
)

my_db = my_client["node-app"]

my_collection = my_db["products"]  # Yoksa bu collection, oluşturur

print(my_db.list_collection_names())

# Veri ekleme
# product = {"name":"Samsung S5", "price": 2000}

# result = my_collection.insert_one(product)  # çok olsa insert_many()

# print(result)
# print(type(result))
# print(result.inserted_id)  # Atadığı oto id

product_list = [
    {"name": "Samsung S6", "price": 3000, "description": "iyi telefon"},
    # {"_id": 1, "name":"Samsung S6", "price": 3000},  # _id ile id atayabiliriz
    {"name": "Samsung S7", "price": 4000, "categories": ["Telefon", "Elektronik"]},
    {"name": "Samsung S8", "price": 5000},
    {"name": "Samsung S9", "price": 6000},
    {"name": "Samsung S10", "price": 7000},
    {"name": "Samsung S11", "price": 8000},
]

result = my_collection.insert_many(product_list)
print(result.inserted_ids)  # çoğul olunca ids
