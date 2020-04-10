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

class Comercio(Resource):

    def get(self, id_comercio):

        comercio = ModeloComercio.query.filter_by(id_comercio=id_comercio).first()

        if comercio:
        
            resultado = {
                "cidade": {
                    "id": comercio.cidade.id_cidade,
                    "nome": comercio.cidade.nome,
                    "comercio":{
                        "id": comercio.id_comercio,
                        "nome": comercio.nome,
                        "email": comercio.email
                    }
                }
            }
            aux_telefone = []
            aux_endereco = []
            aux_atendimento = []
            aux_pagamento = []
            for t in comercio.telefones:
                telefone = {
                    "id": t.id_telefone,
                    "telefone": t.telefone
                }
                aux_telefone.append(telefone)

            for e in comercio.enderecos:
                endereco = {
                    "id": e.id_endereco,
                    "rua": e.rua,
                    "numero": e.numero,
                    "bairro": e.bairro,
                    "complemento": e.complemento,
                    "cep": e.cep
                }
                aux_endereco.append(endereco)

            for a in comercio.formas_atendimento:
                atendimento = {
                    "id": a.id_forma_atendimento,
                    "descricao": a.descricao,
                    "compra_minia": a.compra_minino_pedido,
                    "valor": a.valor
                }
                aux_atendimento.append(atendimento)
            
            for p in comercio.formas_pagamento:
                pagamento = {
                    "id": p.id_forma_pagamento,
                    "descricao": p.descricao
                }
                aux_pagamento.append(pagamento)

            resultado["cidade"]["comercio"]["telefones"] = aux_telefone
            resultado["cidade"]["comercio"]["enderecos"] = aux_endereco
            resultado["cidade"]["comercio"]["atendimentos"] = aux_atendimento
            resultado["cidade"]["comercio"]["pagamentos"] = aux_pagamento

            return  resultado, 200
        return {'erro': 'Comercio nao encontrado'}, 500

class AtendimentoComercio(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('descricao', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('compra_minino_pedido', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('valor', type=str, required=True, help="Esse campo não pode ser deixado em branco.")

    def post(self, id_comercio):
        
        dados = AtendimentoComercio.parser.parse_args()
        
        atendimento = ModeloFormaAtendimento.query.filter_by(descricao=dados['descricao'], comercio_id=id_comercio).first()

        if atendimento:
            return {'erro': 'Forma de atendimento já cadastrada'}, 500
        else:
            try:
                comercio = ModeloComercio.query.filter_by(id_comercio=id_comercio).first()
                atendimento = ModeloFormaAtendimento(descricao=dados['descricao'], compra_minino_pedido=dados['compra_minino_pedido'], valor=dados['valor'], comercio=comercio)
                db.session.add(atendimento)
                db.session.commit()
                resultado = {
                    "comercio": atendimento.comercio.nome,
                    "forma_atendimento": atendimento.descricao
                }

                return resultado, 201
            except:
                return {'erro': 'nao foi possivel cadastrar'}, 500

class PagamentoComercio(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('descricao', type=str, required=True, help="Esse campo não pode ser deixado em branco.")

    def post(self, id_comercio):

        dados = PagamentoComercio.parser.parse_args()

        pagamento = ModeloFormaPagamento.query.filter_by(descricao=dados['descricao'], comercio_id=id_comercio).first()

        if pagamento:
            return {'erro': 'forma de pagamento ja cadastrada'}, 500
        else:
            try:
                comercio = ModeloComercio.query.filter_by(id_comercio=id_comercio).first()
                pagamento = ModeloFormaPagamento(descricao=dados['descricao'], comercio=comercio)
                db.session.add(pagamento)
                db.session.commit()
                resultado = {
                    "comercio": pagamento.comercio.nome,
                    "forma_pagamento": pagamento.descricao
                }

                return resultado, 201
            except:
                return {'erro': 'nao foi possivel cadastrar'}, 500



class TelefoneComercio(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('telefone', type=str, required=True, help="Esse campo não pode ser deixado em branco.")

    def post(self, id_comercio):
        
        dados = TelefoneComercio.parser.parse_args()

        telefone = ModeloTelefoneComercio.query.filter_by(telefone=dados['telefone']).first()

        if telefone:
            return {'erro': 'Telefone já cadastrado'}, 500
        else:
            telefone = ModeloTelefoneComercio(telefone=dados['telefone'], comercio_id=id_comercio)
            db.session.add(telefone)
            db.session.commit()
            resultado = {
                "comercio": telefone.comercio.nome,
                "telefone": telefone.telefone
            }

            return resultado, 201

class EnderecoComercio(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('rua', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('numero', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('bairro', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('complemento', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
    parser.add_argument('cep', type=str, required=True, help="Esse campo não pode ser deixado em branco.")

    def post(self, id_comercio):

        dados = EnderecoComercio.parser.parse_args()
        try:
            endereco = ModeloEnderecoComercio(rua=dados['rua'], numero=dados['numero'], bairro=dados['bairro'], complemento=dados['complemento'], cep=dados['cep'], comercio_id=id_comercio)
            db.session.add(endereco)
            db.session.commit()
            resultado = {
                "nome": endereco.comercio.nome,
                "id_endereco": endereco.id_endereco,
                "rua": endereco.rua,
                "numero": endereco.numero,
                "bairro": endereco.bairro,
                "complemento": endereco.complemento,
                "cep": endereco.cep
            }

            return resultado
        except:
            return {'erro' : 'Por algum motivo ocorreu um erro no servidor'}, 500