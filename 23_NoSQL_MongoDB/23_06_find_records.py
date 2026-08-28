"""Select işlemleri, istenilen kolonları getirme -> .find_one(), .find()"""

import pymongo

my_client = pymongo.MongoClient(
    "mongodb+srv://utkush2_db_user:{password}@cluster0.vwxvp3u.mongodb.net/?appName=Cluster0"
)

my_db = my_client["node-app"]
my_collection = my_db["products"]

result = my_collection.find_one()  # İlk kaydı getirme

print(result)

for record in my_collection.find():  # Filtresiz tüm kayıtlar
    print(record)

print("*" * 100)

# İlki filtreleme ikincisi kolon seçme {} {}
for record in my_collection.find({}, {"_id": 0, "name": 1, "categories": 1}):
    print(record)

# Sadece 0 verirsen istenmeyenler dışı hepsi gelir.
# _id: 0 yapmazsan illa gelir.
# Boş kolonlar da gelmiyor.
