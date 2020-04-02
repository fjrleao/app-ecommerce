from db import db

class PedidoModel(db.Model):

    __tablename__ = 'pedidos'
    id_pedido = db.Column(db.Integer, primary_key=True)
