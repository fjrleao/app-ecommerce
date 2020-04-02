from db import db
from pedido import PedidoModel

class ClienteModel(db.Model):

    __tablename__ = 'users'

    id_user = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(45))


    