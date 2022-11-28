from marshmallow import Schema, fields
import json

class UsuarioSchema(Schema):
    usuario = fields.Str()
    senha = fields.Str()


class Usuario:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
    def toJson(self):
        store_schema = UsuarioSchema()
        bson_example = store_schema.dumps(self)
        data = json.loads(bson_example)
        return data
