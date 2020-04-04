from flask import request
from flask_restful import Resource, reqparse
from models.estado import Cidade, Estado
from db import db

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

    def post(self):
        dados = Estados.parser.parse_args()
        estado = Estado(nome=dados['nome'], sigla=dados['sigla'])
        db.session.add(estado)
        db.session.commit()
        
        return {'success' : 'estado salvo com sucesso'}


class Cidades(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('nome',
                        type=str,
                        required=True,
                        help="Esse campo não pode ser deixado em branco."
                        )

    def post(self, id_estado):
        estado = Estado.query.filter_by(id_estado=id_estado).first()
        dados = Cidades.parser.parse_args()
        cidade = Cidade(nome=dados['nome'], estado=estado)
        db.session.add(cidade)
        db.session.commit()
        return {'ok' : 'cidade salva com sucesso'}