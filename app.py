from flask import Flask, request
from flask_restful import Api
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models.estado import ModeloCidade, ModeloEstado
from models.cliente import ModeloCliente, ModeloEnderecoCliente, ModeloTelefoneCliente
from models.comercio import ModeloCategoriaComercio, ModeloComercio, ModeloEnderecoComercio, ModeloFormaAtendimento, ModeloFormaPagamento, ModeloTelefoneComercio
from models.pedido import ModeloAvaliacao, ModeloEnderecoPresente, ModeloPedido, ModeloPresente, ModeloProdutosPedido
from models.produto import ModeloCategoriaProduto, ModeloProduto
from controllers.api.estado import Estados, Cidades, Cidade

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

#rotas da API
api.add_resource(Estados, '/estados/')
api.add_resource(Cidades, '/estado/<int:id_estado>/cidades/')
api.add_resource(Cidade, '/cidade/<int:id_cidade>/')

#rotas da aplicaçao web
#app.register_blueprint(hello_page)

from db import db

def criar_app():
    db.init_app(app)
    return app


if __name__ == "__main__":
    
    app = criar_app()
    
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()
