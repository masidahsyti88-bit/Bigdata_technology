from pymongo import MongoClient

uri = "mongodb+srv://masidahsyti:bigdata1@cluster0.raeo1dz.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(uri)
    print("Koneksi berhasil!")
    print("List database:")
    print(client.list_database_names())
except Exception as e:
    print("Koneksi gagal:", e)