from flask import request
from flask_restful import Resource
from models.estado import Cidade, Estado

class Estados(Resource):
    def get(self):
        estados = Estado.query.all()
        for estado in estados:
            print(estado.nome)
        return {'ok' : 'ok'}