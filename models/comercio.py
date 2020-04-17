from db import db
from werkzeug.security import generate_password_hash, check_password_hash

class ModeloCategoriaComercio(db.Model):

    __tablename__ = 'categoria_comercio'

    id_categoria = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(120), nullable=False)
    comercios = db.relationship('ModeloComercio', backref='categoria_comercio', lazy=False)

class ModeloComercio(db.Model):

    __tablename__ = 'comercio'

    id_comercio = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    cpf_cnpj = db.Column(db.String(25), nullable=False, unique=True)
    senha = db.Column(db.String(260), nullable=False)
    imagem = db.Column(db.String(80))
    funcionamento = db.Column(db.Boolean, default=False, nullable=False)
    ativo = db.Column(db.Boolean, default=True, nullable=False)
    cidade_id = db.Column(db.Integer, db.ForeignKey('cidade.id_cidade'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria_comercio.id_categoria'), nullable=False)
    formas_atendimento = db.relationship('ModeloFormaAtendimento', backref='comercio', lazy=False)
    formas_pagamento = db.relationship('ModeloFormaPagamento', backref='comercio', lazy=False)
    telefones = db.relationship('ModeloTelefoneComercio', backref='comercio', lazy=False)
    enderecos = db.relationship('ModeloEnderecoComercio', backref='comercio', lazy=False)
    categorias = db.relationship('ModeloCategoriaProduto', backref='comercio', lazy=False)
    produtos = db.relationship('ModeloProduto', backref='comercio', lazy=False)
    pedidos = db.relationship('ModeloPedido', backref='comercio', lazy=False)

    def __init__(self, nome, descricao, email, cpf_cnpj, senha, cidade, categoria):
        self.nome = nome
        self.descricao = descricao
        self.email = email
        self.cpf_cnpj = cpf_cnpj
        self.senha = generate_password_hash(senha)
        self.cidade_id = cidade
        self.categoria_id = categoria

    def verificaSenha(self, senha):
        return check_password_hash(self.senha, senha)


class ModeloEnderecoComercio(db.Model):

    __tablename__ = 'endereco_comercio'

    id_endereco = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rua = db.Column(db.String(80), nullable=False)
    numero = db.Column(db.String(25), nullable=False)
    bairro = db.Column(db.String(80), nullable=False)
    complemento = db.Column(db.String(80), nullable=False)
    cep = db.Column(db.String(25), nullable=False)
    comercio_id = db.Column(db.Integer, db.ForeignKey('comercio.id_comercio'), nullable=False)


class ModeloTelefoneComercio(db.Model):

    __tablename__ = 'telefone_comercio'

    id_telefone = db.Column(db.Integer, autoincrement=True, primary_key=True)
    telefone = db.Column(db.String(25), nullable=False, unique=True)
    comercio_id = db.Column(db.Integer, db.ForeignKey('comercio.id_comercio'), nullable=False)

class ModeloFormaAtendimento(db.Model):

    __tablename__ = 'forma_atendimento'

    id_forma_atendimento = db.Column(db.Integer, autoincrement=True, primary_key=True)
    descricao = db.Column(db.String(45), nullable=False)
    valor = db.Column(db.Float(precision=2), nullable=False)
    compra_minino_pedido = db.Column(db.Float(precision=2), nullable=False)
    comercio_id = db.Column(db.Integer, db.ForeignKey('comercio.id_comercio'), nullable=False)

class ModeloFormaPagamento(db.Model):

    __tablename__ = 'forma_pagamento'

    id_forma_pagamento = db.Column(db.Integer, autoincrement=True, primary_key=True)
    descricao = db.Column(db.String(45), nullable=False)
    comercio_id = db.Column(db.Integer, db.ForeignKey('comercio.id_comercio'), nullable=False)