from db import db

class ClienteModel(db.Model):

    __tablename__ = 'clientes'

    id_user = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(45))

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def save(self):
        db.session.add(self)
        db.session.commit()

    