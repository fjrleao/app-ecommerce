from db import db
from werkzeug.security import check_password_hash, generate_password_hash

class ModeloCliente(db.Model):

    __tablename__ = 'cliente'

    id_cliente = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    senha = db.Column(db.String(260), nullable=False)
    imagem = db.Column(db.String(80))
    ativo = db.Column(db.Boolean, default=True, nullable=False)
    cidade_id = db.Column(db.Integer, db.ForeignKey('cidade.id_cidade'), nullable=False)
    enderecos = db.relationship('ModeloEnderecoCliente', backref='cliente', lazy=False)
    telefones = db.relationship('ModeloTelefoneCliente', backref='cliente', lazy=False)
    pedidos = db.relationship('ModeloPedido', backref='cliente', lazy=False)

    def __init__ (self, nome, email, senha, cidade):
        self.nome = nome
        self.email = email
        self.senha = generate_password_hash(senha)
        self.cidade_id = cidade

    def verificaSenha(self, senha):
        return check_password_hash(self.senha, senha)

class ModeloEnderecoCliente(db.Model):

    __tablename__ = 'endereco_cliente'

    id_endereco = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rua = db.Column(db.String(80), nullable=False)
    numero = db.Column(db.String(25), nullable=False)
    bairro = db.Column(db.String(80), nullable=False)
    complemento = db.Column(db.String(80), nullable=False)
    cep = db.Column(db.String(25), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'), nullable=False)

class ModeloTelefoneCliente(db.Model):

    __tablename__ = 'telefone_cliente'

    id_telefone = db.Column(db.Integer, autoincrement=True, primary_key=True)
    telefone = db.Column(db.String(25), nullable=False, unique=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'), nullable=False)