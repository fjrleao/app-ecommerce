from db import db

class Cliente(db.Model):

    __tablename__ = 'cliente'

    id_cliente = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    senha = db.Column(db.String(120), nullable=False)
    imagem = db.Column(db.String(80))
    ativo = db.Column(db.Boolean, default=True, nullable=False)
    cidade_id = db.Column(db.Integer, db.ForeignKey('cidade.id_cidade'), nullable=False)
    enderecos = db.relationship('EnderecoCliente', backref='cliente', lazy=False)
    telefones = db.relationship('TelefoneCliente', backref='cliente', lazy=False)
    pedidos = db.relationship('Pedido', backref='cliente', lazy=False)

class EnderecoCliente(db.Model):

    __tablename__ = 'endereco_cliente'

    id_endereco = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rua = db.Column(db.String(80), nullable=False)
    numero = db.Column(db.String(25), nullable=False)
    bairro = db.Column(db.String(80), nullable=False)
    complemento = db.Column(db.String(80), nullable=False)
    cep = db.Column(db.String(25), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'), nullable=False)

class TelefoneCliente(db.Model):

    __tablename__ = 'telefone_cliente'

    id_telefone = db.Column(db.Integer, autoincrement=True, primary_key=True)
    telefone = db.Column(db.String(25), nullable=False, unique=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'), nullable=False)