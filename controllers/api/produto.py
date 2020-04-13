from db import db
from models.produto import ModeloCategoriaProduto, ModeloProduto, ModeloDetalheProduto
from models.comercio import ModeloComercio
from flask_restful import Resource, reqparse, request

class CategoriasProduto(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('nome', type=str, required=True, help="Esse campo não pode ser deixado em branco.")

    def post(self, id_comercio):

        dados = CategoriasProduto.parser.parse_args()

        try:
            comercio = ModeloComercio.query.filter_by(id_comercio=id_comercio).first()
            categoria = ModeloCategoriaProduto.query.filter_by(nome=dados['nome'], comercio=comercio).first()
            if categoria:
                return {'erro' : 'categoria ja cadastrada'}, 500
            else:
                categoria = ModeloCategoriaProduto(nome=dados['nome'], comercio=comercio)
                db.session.add(categoria)
                db.session.commit()
                resultado = {
                    "comercio":categoria.comercio.nome,
                    "id_categoria": categoria.id_categoria,
                    "nome" : categoria.nome
                }
                return resultado, 201

        except:
            return {'erro' : 'erro no servidor'}, 500
    
    def get(self, id_comercio):

        try:
            comercio = ModeloComercio.query.filter_by(id_comercio=id_comercio).first()
            categorias = ModeloCategoriaProduto.query.filter_by(comercio=comercio)

            resultado = {
                "comercio":{
                    "id" : comercio.id_comercio,
                    "nome":comercio.nome,
                    "email": comercio.email
                }
            }
            aux_categoria = []
            for c in categorias:
                categoria = {
                    "id": c.id_categoria,
                    "nome": c.nome
                }
                aux_categoria.append(categoria)

            resultado["comercio"]["categorias"] = aux_categoria

            return resultado, 200

        except:
            return {'erro' : 'erro no servidor'}, 500

class Produtos(Resource):

    def post(self, id_comercio, id_categoria):

        parser = reqparse.RequestParser()
        parser.add_argument('codigo_barra', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
        parser.add_argument('nome', type=str, required=True, help="Esse campo não pode ser deixado em branco.")
        parser.add_argument('preco', type=float, required=True, help="Esse campo não pode ser deixado em branco.")
        parser.add_argument('quantidade', type=int, required=True, help="Esse campo não pode ser deixado em branco.")
        parser.add_argument('desconto', type=float, required=True, help="Esse campo não pode ser deixado em branco.")
        dados = parser.parse_args()

        produto = ModeloProduto.query.filter_by(codigo_barra=dados['codigo_barra']).first()
        if produto:
            return {'erro' : 'produto com esse codigo ja cadastrado'}, 500
        else:
            try:
                comercio = ModeloComercio.query.filter_by(id_comercio=id_comercio).first()
                categoria = ModeloCategoriaProduto.query.filter_by(id_categoria=id_categoria).first()
                produto = ModeloProduto(
                    codigo_barra=dados['codigo_barra'],
                    nome=dados['nome'],
                    preco=dados['preco'],
                    quantidade=dados['quantidade'],
                    desconto=dados['desconto'],
                    comercio=comercio,
                    categoria_produto=categoria
                )
                db.session.add(produto)
                db.session.commit()
                resultado = {
                    "categoria":{
                        "id":produto.categoria_produto.id_categoria,
                        "nome":produto.categoria_produto.nome,
                        "produto":{
                            "codigo_barra": produto.codigo_barra,
                            "nome": produto.nome,
                            "preco": produto.preco
                        }
                    }
                }
                return resultado, 201
            except:
                return {'erro' : 'erro no servidor'}, 500
    
    def get(self, id_comercio, id_categoria):
        try:
            produtos = ModeloProduto.query.filter_by(comercio_id=id_comercio, categoria_id=id_categoria)

            resultado = {
                "comercio":{
                    "id":produtos[0].comercio.id_comercio,
                    "nome":produtos[0].comercio.nome,
                    "categoria":{
                        "id":produtos[0].categoria_produto.id_categoria,
                        "nome":produtos[0].categoria_produto.nome,
                    }
                }
            }

            aux_produto = []
            for p in produtos:
                aux_detalhe = []
                produto = {
                    "id" : p.id_produto,
                    "codigo_barra": p.codigo_barra,
                    "nome": p.nome,
                    "preco": p.preco
                }
                for d in p.detalhes:
                    detalhe = {
                        "nome" : d.nome,
                        "descricao":d.descricao
                    }
                    aux_detalhe.append(detalhe)
                produto["detalhes"] = aux_detalhe
                aux_produto.append(produto)

            resultado["comercio"]["categoria"]["produtos"] = aux_produto

            return resultado, 200
        except:
            return {'erro': 'erro no servidor'}, 500

class DetalhesProduto(Resource):

    def post(self, id_produto):

        dados = request.get_json()
        
        produto = ModeloProduto.query.filter_by(id_produto=id_produto).first()

        if produto:
            aux_resultado = []
            for d in dados:
                detalhe = ModeloDetalheProduto(nome=d['nome'], descricao=d['descricao'], produto=produto)
                db.session.add(detalhe)
                db.session.commit()
                detalhe = {
                    "nome" : d['nome'],
                    "descricao" : d['descricao']
                }
                aux_resultado.append(detalhe)

            resultado = {
                "produto":{
                    "nome": produto.nome,
                    "preco" : produto.preco,
                    "detalhes": aux_resultado
                }
            }

            return resultado, 201

        else:
            return {'erro': 'produto nao existe'}, 500
