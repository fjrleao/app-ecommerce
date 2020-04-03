from db import db

class ProdutosPedido(db.Model):

    __tablename__ = 'produtos_pedidos'

    id_produtos_pedidos = db.Column(db.Integer, autoincrement=True, primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)
    sub_total = db.Column(db.Integer, nullable=False)

    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id_pedido'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id_produto'), nullable=False)

    produto = db.relationship('Produto', backref='produtos_pedidos')
    pedido = db.relationship('Pedido', backref='produtos_pedidos')

class Pedido(db.Model):

    __tablename__ = 'pedido'

    id_pedido = db.Column(db.Integer, autoincrement=True, primary_key=True)
    data = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(25), nullable=False)
    tipo_pagamento = db.Column(db.String(25), nullable=False)
    tipo_atendimento = db.Column(db.String(25), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'), nullable=False)
    comercio_id = db.Column(db.Integer, db.ForeignKey('comercio.id_comercio'), nullable=False)
    presente = db.relationship('Presente', backref='pedido', lazy=False, uselist=False)
    avaliacao = db.relationship('Avaliacao', backref='pedido', lazy=False, uselist=False)
    produtos = db.relationship('Produto', secondary='produtos_pedidos')

class Presente(db.Model):

    __tablename__ = 'presente'

    id_presente = db.Column(db.Integer, autoincrement=True, primary_key=True)
    descricao = db.Column(db.String(120))
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id_pedido'), nullable=False)
    endereco = db.relationship('EnderecoPresente', backref='presente', uselist=False)

class EnderecoPresente(db.Model):

    __tablename__ = 'endereco_presente'

    id_endereco = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rua = db.Column(db.String(80), nullable=False)
    numero = db.Column(db.String(25), nullable=False)
    bairro = db.Column(db.String(80), nullable=False)
    complemento = db.Column(db.String(80), nullable=False)
    cep = db.Column(db.String(25), nullable=False)
    presente_id = db.Column(db.Integer, db.ForeignKey('presente.id_presente'), nullable=False)

class Avaliacao(db.Model):

    __tablename__ = 'avaliacao'

    id_avaliacao = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nota_cliente = db.Column(db.Integer, nullable=False)
    nota_comercio = db.Column(db.Integer, nullable=False)
    comentario_cliente = db.Column(db.String(80))
    comentario_comercio = db.Column(db.String(80))
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id_pedido'), nullable=False)
