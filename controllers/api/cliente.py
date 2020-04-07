from flask import request, json
from flask_restful import Resource, reqparse
from models.cliente import ModeloCliente, ModeloTelefoneCliente, ModeloEnderecoCliente
from db import db

class TelefoneCliente(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('telefone', type=str, required=True, help="Esse campo não pode ser deixado em branco.")

    def post(self, id_cliente):

        dados = TelefoneCliente.parser.parse_args()

        telefone = ModeloTelefoneCliente.query.filter_by(telefone=dados['telefone']).first()

        if telefone:
            return {'erro': 'Telefone já foi cadastrado'}
        else:

            telefone = ModeloTelefoneCliente(telefone=dados['telefone'], cliente_id=id_cliente)
            db.session.add(telefone)
            db.session.commit()
            resultado = {
                "nome": telefone.cliente.nome,
                "id_telefone": telefone.id_telefone,
                "telefone": telefone.telefone
            }

            return resultado

class EnderecoCliente(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('rua', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('numero', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('bairro', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('complemento', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('cep', type=str, required=True, help="Esse campo não pode ser deixado em branco.")

    def post(self, id_cliente):

        dados = EnderecoCliente.parser.parse_args()

        endereco = ModeloEnderecoCliente(rua=dados['rua'], numero=dados['numero'], bairro=dados['bairro'], complemento=dados['complemento'], cep=dados['cep'], cliente_id=id_cliente)
        db.session.add(endereco)
        db.session.commit()
        resultado = {
            "nome": endereco.cliente.nome,
            "id_endereco": endereco.id_endereco,
            "rua": endereco.rua,
            "numero": endereco.numero,
            "bairro": endereco.bairro,
            "complemento": endereco.complemento,
            "cep": endereco.cep
        }

        return resultado


class Cliente(Resource):

    def get(self, id_cliente):

        cliente = ModeloCliente.query.filter_by(id_cliente=id_cliente).first()
        
        if cliente:

            resultado = {
                "cidade": {
                    "id": cliente.cidade.id_cidade,
                    "nome": cliente.cidade.nome,
                    "cliente":{
                        "id": cliente.id_cliente,
                        "nome": cliente.nome,
                        "email": cliente.email
                    }
                }
            }
            aux_telefone = []
            aux_endereco = []
            for t in cliente.telefones:
                telefone = {
                    "id": t.id_telefone,
                    "telefone": t.telefone
                }
                aux_telefone.append(telefone)

            for e in cliente.enderecos:
                endereco = {
                    "id": e.id_endereco,
                    "rua": e.rua,
                    "numero": e.numero,
                    "bairro": e.bairro,
                    "complemento": e.complemento,
                    "cep": e.cep
                }
                aux_endereco.append(endereco)

            resultado["cidade"]["cliente"]["telefones"] = aux_telefone
            resultado["cidade"]["cliente"]["enderecos"] = aux_endereco

            return  resultado, 200
        return {'erro' : 'cliente não encontrado'} , 500

class Clientes(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('nome', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('email', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('senha', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
        

    def post(self, id_cidade):

        dados = Clientes.parser.parse_args()

        cliente = ModeloCliente.query.filter_by(email=dados['email']).first()
        if cliente:
            return {'erro': 'Cliente já cadastrado com esse email'}, 500
        else:
            cliente = ModeloCliente(nome=dados['nome'], email=dados['email'], senha=dados['senha'], cidade_id=id_cidade)
            db.session.add(cliente)
            db.session.commit()
            resultado = {
                "cidade": {
                    "id": cliente.cidade.id_cidade,
                    "nome": cliente.cidade.nome,
                },
                "cliente": {
                    "id": cliente.id_cliente,
                    "nome": cliente.nome,
                    "email": cliente.email,
                }
            }
            return resultado, 201
    
    def get(self, id_cidade):

        clientes = ModeloCliente.query.filter_by(cidade_id=id_cidade)

        resultado = {
            "nome_cidade" : clientes[0].cidade.nome
        }
        aux = []
        for c in clientes:
            cliente = {
                "nome": c.nome,
                "email": c.email
            }
            aux.append(cliente)

        resultado["clientes"] = aux

        return resultado, 200


