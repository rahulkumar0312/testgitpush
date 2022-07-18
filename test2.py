import pymongo
client = pymongo.MongoClient("mongodb+srv://rahulkumar0312:Qwerty2022@cluster0.acf8rgs.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"rahul",
    "email" : "rahul@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )