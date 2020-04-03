from db import db

class Estado(db.Model):

    __tablename__ = 'estado'

    id_estado = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(45), nullable=False, unique=True)
    sigla = db.Column(db.String(3), nullable=False, unique=True)
    cidades = db.relationship('Cidade', backref='estado', lazy=False)

class Cidade(db.Model):

    __tablename__ = 'cidade'

    id_cidade = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(45))
    estado_id = db.Column(db.Integer, db.ForeignKey('estado.id_estado'), nullable=False)
    comercios = db.relationship('Comercio', backref='cidade', lazy=False)
