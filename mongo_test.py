import pymongo
from marshmallow import Schema, fields, post_load

import json

class Person:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

class StoreSchema(Schema):
    usuario = fields.Str()
    senha = fields.Str()

    @post_load
    def make_store(self, data, **kwargs):
        return Person(**data)


p1 = Person("Vitoria", "12345")
myclient = pymongo.MongoClient("mongodb://quiz:quizadmin@18.231.78.22:27017/quiz")

mydb = myclient["quiz"]
mycol = mydb["usuarios"]
store_schema = StoreSchema()
bson_example = store_schema.dumps(p1) # Serializa
data = json.loads(bson_example)

print(data)
finded = mycol.count_documents({"usuario": data['usuario']})
print(finded)
mycol.update_one({"usuario": data['usuario']}, {"$set": data}, upsert=True)

for x in mycol.find({"usuario": "Vitoria"}, {"_id":0}).limit(1):
    print(x.get('senha'))

