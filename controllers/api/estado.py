from flask import request
from flask_restful import Resource, reqparse
from models.estado import ModeloEstado, ModeloCidade
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
        estados = ModeloEstado.query.all()
        resultado = []
        for e in estados:
            estado = {
                "id" : e.id_estado,
                "nome" : e.nome,
                "sigla" : e.sigla
            }
            resultado.append(estado)
        return resultado

    def post(self):
        dados = Estados.parser.parse_args()
        estado = ModeloEstado.query.filter_by(nome=dados['nome']).first()
        if estado:
            return {'erro' : 'Estado já cadastrado'}, 500
        else:
            estado = ModeloEstado(nome=dados['nome'], sigla=dados['sigla'])
            db.session.add(estado)
            db.session.commit()
            resultado = {}
            resultado["id"] = estado.id_estado
            resultado["nome"] = estado.nome
            resultado["sigla"] = estado.sigla
            return resultado, 201


class Cidade(Resource):
    
    def get(self, id_cidade):
        resultado = {}
        try:
            cidade = ModeloCidade.query.filter_by(id_cidade=id_cidade).first()
            resultado["id"] = cidade.id_cidade
            resultado["nome"] = cidade.nome
            return resultado, 200
        except:
            return {'erro' : 'Cidade não encontrada'}, 404
        

class Cidades(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('nome',
                        type=str,
                        required=True,
                        help="Esse campo não pode ser deixado em branco."
                        )

    def post(self, id_estado):
        #estado = ModeloEstado.query.filter_by(id_estado=id_estado).first()
        dados = Cidades.parser.parse_args()
        cidade = ModeloCidade.query.filter_by(nome=dados['nome']).first()
        if cidade:
            return {'erro' : 'Cidade já existe'}, 500
        else:
            cidade = ModeloCidade(nome=dados['nome'], estado=estado)
            db.session.add(cidade)
            db.session.commit()
            resultado = {}
            resultado["id_estado"] = estado.id_estado
            resultado["nome_estado"] = estado.nome
            resultado["id_cidade"] = cidade.id_cidade
            resultado["nome_cidade"] = cidade.nome
            return resultado, 201

    def get(self, id_estado):
        try:
            estado = ModeloEstado.query.filter_by(id_estado=id_estado).first()
            resultado = {}
            resultado["id"] = estado.id_estado
            resultado["nome"] = estado.nome
            resultado["sigla"] = estado.sigla
            aux = []
            for c in estado.cidades:
                cidade = {
                    "id" : c.id_cidade,
                    "nome" : c.nome
                }
                aux.append(cidade)
            resultado["cidades"] = aux
            return resultado, 200
        except:
            return {'erro' : 'estado não encontrado'}, 404