from db import db

class ModeloEstado(db.Model):

    __tablename__ = 'estado'

    id_estado = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(45), nullable=False, unique=True)
    sigla = db.Column(db.String(3), nullable=False, unique=True)
    cidades = db.relationship('ModeloCidade', backref='estado', lazy=False)

class ModeloCidade(db.Model):

    __tablename__ = 'cidade'

    id_cidade = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(45))
    estado_id = db.Column(db.Integer, db.ForeignKey('estado.id_estado'), nullable=False)
    comercios = db.relationship('ModeloComercio', backref='cidade', lazy=False)
    clientes = db.relationship('ModeloCliente', backref='cidade', lazy=False)