from db import db

class CategoriaComercio(db.Model):

    __tablename__ = 'categoria_comercio'

    id_categoria_comercio = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(120), nullable=False)
    comercios = db.relationship('Comercio', backref='categoria_comercio', lazy=False)

class Comercio(db.Model):

    __tablename__ = 'comercio'

    id_comercio = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    senha = db.Column(db.String(120), nullable=False)
    imagem = db.Column(db.String(80))
    funcionamento = db.Column(db.Boolean, default=False, nullable=False)
    ativo = db.Column(db.Boolean, default=True, nullable=False)
    cidade_id = db.Column(db.Integer, db.ForeignKey('cidade.id_cidade'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria_comercio.id_categoria_comercio', nullable=False))
    formas_atendimento = db.relationship('FormaAtendimento', backref='comercio', lazy=False)
    formas_pagamento = db.relationship('FormaPagamento', backref='comercio', lazy=False)
    telefones = db.relationship('TelefoneComercio', backref='comercio', lazy=False)
    enderecos = db.relationship('EnderecoComercio', backref='comercio', lazy=False)

class EnderecoComercio(db.Model):

    __tablename__ = 'endereco_comercio'

    id_endereco = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rua = db.Column(db.String(80), nullable=False)
    numero = db.Column(db.String(25), nullable=False)
    bairro = db.Column(db.String(80), nullable=False)
    complemento = db.Column(db.String(80), nullable=False)
    cep = db.Column(db.String(25), nullable=False)
    comercio_id = db.Column(db.Integer, db.ForeignKey('comercio.id_comercio'), nullable=False)


class TelefoneComercio(db.Model):

    __tablename__ = 'telefone_comercio'

    id_telefone = db.Column(db.Integer, autoincrement=True, primary_key=True)
    telefone = db.Column(db.String(25), nullable=False, unique=True)
    comercio_id = db.Column(db.Integer, db.ForeignKey('comercio.id_comercio'), nullable=False)

class FormaAtendimento(db.Model):

    __tablename__ = 'forma_atendimento'

    id_forma_atendimento = db.Column(db.Integer, autoincrement=True, primary_key=True)
    descricao = db.Column(db.String(45), nullable=False)
    comercio_id = db.Column(db.Integer, db.ForeignKey('comercio.id_comercio'), nullable=False)

class FormaPagamento(db.Model):

    __tablename__ = 'forma_pagamento'

    id_forma_pagamento = db.Column(db.Integer, autoincremet=True, primary_key=True)
    descricao = db.Column(db.String(45), nullable=False)
    comercio_id = db.Column(db.Integer, db.ForeignKey('comercio.id_comercio'), nullable=False)