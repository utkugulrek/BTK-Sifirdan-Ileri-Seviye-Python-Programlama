"""MongoDB local ve cloud bağlanma"""

import pymongo

# Localhost
my_client = pymongo.MongoClient("mongodb://localhost:27017")

my_db = my_client["node-app"]

print(my_client.list_database_names())  # Server'deki db isimleri

# Cloud
my_client = pymongo.MongoClient(
    "mongodb+srv://utkush2_db_user:{password}@cluster0.vwxvp3u.mongodb.net/node-app?appName=Cluster0"
)

print(my_client.list_database_names())
# Böyle de oluyormuş
# Bağlantıyı kur
client = pymongo.MongoClient(
    "mongodb+srv://utkush2_db_user:{password}@cluster0.vwxvp3u.mongodb.net/?appName=Cluster0"
)

# Veri tabanını Python kodu içinde seç
db = client["node-app"]
