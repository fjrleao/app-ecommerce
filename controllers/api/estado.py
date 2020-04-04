from flask import request
from flask_restful import Resource, reqparse
from models.estado import Cidade, Estado

class Estados(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('nome',
                        type=str,
                        required=True,
                        help="Esse campo não pode ser deixado em branco."
                        )

    parser.add_argument('sigla',
                        type=str,
                        required=True,
                        help="Esse campo não pode ser deixado em branco."
                        )

    def get(self):
        estados = Estado.query.all()
        for estado in estados:
            print(estado.nome)
        return {'ok' : 'ok'}