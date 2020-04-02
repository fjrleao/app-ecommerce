from db import db

class ProdutoModel(db.Model):
    __tablename__ = 'produtos'
    
    id_produto = db.Column(db.String(30), primary_key=True)
    nome = db.Column(db.String(45))
    descricao = db.Column(db.String(120))

class ProdutoPedidoModel(db.Model):
    __tablename__ = 'produtos_pedidos'

    quantidade = db.Column(db.Integer)