from flask import Flask, request
from flask_restful import Api
from controllers.cliente import User, Users
from models.cliente import ClienteModel
from models.pedido import PedidoModel
from models.produto import ProdutoModel, ProdutoPedidoModel
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

'''@app.before_first_request
def create_tables():
    db.create_all'''

api.add_resource(User, "/users/<int:id>")
api.add_resource(Users, "/users/")

if __name__ == "__main__":
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()
