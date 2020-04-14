from db import db

class ModeloProdutosPedido(db.Model):

    __tablename__ = 'produtos_pedidos'

    id_produtos_pedidos = db.Column(db.Integer, autoincrement=True, primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)
    sub_total = db.Column(db.Integer, nullable=False)

    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id_pedido'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id_produto'), nullable=False)

    produto = db.relationship('ModeloProduto', backref='produtos_pedidos')
    pedido = db.relationship('ModeloPedido', backref='produtos_pedidos')

class ModeloPedido(db.Model):

    __tablename__ = 'pedido'

    id_pedido = db.Column(db.Integer, autoincrement=True, primary_key=True)
    data = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(25), nullable=False)
    tipo_pagamento = db.Column(db.String(25), nullable=False)
    tipo_atendimento = db.Column(db.String(25), nullable=False)
    observacao = db.Column(db.String(160))
    presente = db.Column(db.Boolean, default=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'), nullable=False)
    comercio_id = db.Column(db.Integer, db.ForeignKey('comercio.id_comercio'), nullable=False)
    mensagens = db.relationship('ModeloMensagem', backref='mensagem_pedido', lazy=False)
    presente = db.relationship('ModeloPresente', backref='pedido', lazy=False, uselist=False)
    avaliacao = db.relationship('ModeloAvaliacao', backref='pedido', lazy=False, uselist=False)
    produtos = db.relationship('ModeloProduto', secondary='produtos_pedidos')
    
class ModeloMensagem(db.Model):

    __tablename__ = 'mensagem_pedido'

    id_mensagem = db.Column(db.Integer, autoincrement=True, primary_key=True)
    texto = db.Column(db.String(160), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    remetente = db.Column(db.String(25), nullable=False)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id_pedido'), nullable=False)

class ModeloPresente(db.Model):

    __tablename__ = 'presente'

    id_presente = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rua = db.Column(db.String(80))
    numero = db.Column(db.String(25))
    bairro = db.Column(db.String(80))
    complemento = db.Column(db.String(80))
    cep = db.Column(db.String(25))
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id_pedido'), nullable=False)

class ModeloAvaliacao(db.Model):

    __tablename__ = 'avaliacao'

    id_avaliacao = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nota_cliente = db.Column(db.Integer, nullable=False)
    nota_comercio = db.Column(db.Integer, nullable=False)
    comentario_cliente = db.Column(db.String(80))
    comentario_comercio = db.Column(db.String(80))
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id_pedido'), nullable=False)
