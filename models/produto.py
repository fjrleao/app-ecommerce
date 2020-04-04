from db import db

class ModeloCategoriaProduto(db.Model):

    __tablename__ = 'categoria_produto'

    id_categoria = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    comercio_id = db.Column(db.Integer, db.ForeignKey('comercio.id_comercio'), nullable=False)
    produtos = db.relationship('ModeloProduto', backref='categoria_produto', lazy=False)

class ModeloProduto(db.Model):

    __tablename__ = 'produto'

    id_produto = db.Column(db.Integer, autoincrement=True, primary_key=True)
    codigo_barra = db.Column(db.String(45), nullable=False)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(120), nullable=False)
    preco = db.Column(db.Float(precision=2), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    imagem = db.Column(db.String(80))
    ativo = db.Column(db.Boolean, default=True, nullable=False)
    desconto = db.Column(db.Float(precision=2))
    comercio_id = db.Column(db.Integer, db.ForeignKey('comercio.id_comercio'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria_produto.id_categoria'), nullable=False)
    pedidos = db.relationship('ModeloPedido', secondary='produtos_pedidos')