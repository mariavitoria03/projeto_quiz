from db_functions import db_connection
from objetos.Usuario import *
def usuario_existe(user):
    mycol = db_connection("usuarios")
    count = mycol.count_documents({"usuario": user.usuario})
    if count == 0:
        return 0
    else:
        return 1


def criar_usuario(user):
    user_json = user.toJson()
    print(user_json)
    mycol = db_connection("usuarios")
    mycol.update_one({"usuario": user_json['usuario']}, {"$set": user_json}, upsert=True)
def verificar_senha(user):
    mycol = db_connection("usuarios")
    for x in mycol.find({"usuario": user.usuario}, {"_id": 0}).limit(1):
        if x.get('senha') == user.senha:
            return 1
    return 0



