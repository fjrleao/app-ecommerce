from models.comercio import ModeloCategoriaComercio, ModeloComercio, ModeloEnderecoComercio, ModeloFormaAtendimento, ModeloFormaPagamento, ModeloTelefoneComercio
from db import db
from flask_restful import Resource, reqparse

class CategoriaComercio(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('nome', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('descricao', type=str, required=True, help="Esse campo não pode ser deixado em branco")

    def post(self):

        dados = CategoriaComercio.parser.parse_args()

        categoria = ModeloCategoriaComercio.query.filter_by(nome=dados['nome']).first()

        if categoria:
            return {'erro' : 'Categoria já cadastrada'}, 500
        else:
            categoria = ModeloCategoriaComercio(nome=dados['nome'], descricao=dados['descricao'])
            db.session.add(categoria)
            db.session.commit()
            resultado = {
                "id": categoria.id_categoria,
                "nome": categoria.nome,
                "descricao": categoria.descricao
            }
            return resultado, 201

    def get(self):

        categorias = ModeloCategoriaComercio.query.all()
        resultado = []
        for c in categorias:
            categoria = {
                "id": c.id_categoria,
                "nome": c.nome,
                "descricao": c.descricao
            }
            resultado.append(categoria)

        return resultado, 200

class Comercios(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('nome', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('descricao', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('email', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('cpf_cnpj', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('senha', type=str, required=True, help="Esse campo não pode ser deixado em branco.")

    def post(self, id_categoria, id_cidade):

        dados = Comercios.parser.parse_args()

        nome_comercio = ModeloComercio.query.filter_by(nome=dados['nome']).first()
        cnpj_comercio = ModeloComercio.query.filter_by(cpf_cnpj=dados['cpf_cnpj']).first()
        email_comercio = ModeloComercio.query.filter_by(email=dados['email']).first()

        if nome_comercio or cnpj_comercio or email_comercio:
            return {'erro' : 'Comercio com esses dados já existe'}, 500
        else:

            comercio = ModeloComercio(nome=dados['nome'],
                                    descricao=dados['descricao'],
                                    email=dados['email'],
                                    cpf_cnpj=dados['cpf_cnpj'],
                                    senha=dados['senha'],
                                    cidade_id=id_cidade,
                                    categoria_id=id_categoria)
            db.session.add(comercio)
            db.session.commit()
            resultado = {
                "cidade": comercio.cidade.nome,
                "categoria": comercio.categoria_comercio.nome,
                "comercio": {
                    "nome": comercio.nome,
                    "descricao": comercio.descricao,
                    "email": comercio.email,
                    "cpf_cnpj": comercio.cpf_cnpj
                }
            }

            return resultado, 201

    def get(self, id_categoria, id_cidade):

        comercios = ModeloComercio.query.filter_by(cidade_id=id_cidade, categoria_id=id_categoria)
        resultado = []
        for c in comercios:
            comercio = {
                "id": c.id_comercio,
                "nome": c.nome,
                "descricao": c.descricao,
                "email": c.email,
            }
            resultado.append(comercio)

        return resultado, 200
