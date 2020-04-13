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
from controllers.api.cliente import Clientes, Cliente, TelefoneCliente, EnderecoCliente
from controllers.api.comercio import CategoriaComercio, Comercios, TelefoneComercio, EnderecoComercio, Comercio, AtendimentoComercio, PagamentoComercio
from controllers.api.produto import CategoriasProduto, Produtos, DetalhesProduto

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

#rotas da API
api.add_resource(Estados, '/estado/')
api.add_resource(Cidades, '/estado/<int:id_estado>/cidade/')
api.add_resource(Cidade, '/cidade/<int:id_cidade>/')
api.add_resource(Clientes, '/cidade/<int:id_cidade>/cliente/')
api.add_resource(Cliente, '/cliente/<int:id_cliente>/')
api.add_resource(TelefoneCliente, '/cliente/<int:id_cliente>/telefone/')
api.add_resource(EnderecoCliente, '/cliente/<int:id_cliente>/endereco/')
api.add_resource(CategoriaComercio, '/categoria_comercio/')
api.add_resource(Comercios, '/cidade/<int:id_cidade>/categoria_comercio/<int:id_categoria>/comercio/')
api.add_resource(TelefoneComercio, '/comercio/<int:id_comercio>/telefone/')
api.add_resource(EnderecoComercio, '/comercio/<int:id_comercio>/endereco/')
api.add_resource(Comercio, '/comercio/<int:id_comercio>/')
api.add_resource(AtendimentoComercio, '/comercio/<int:id_comercio>/atendimento/')
api.add_resource(PagamentoComercio, '/comercio/<int:id_comercio>/pagamento/')
api.add_resource(CategoriasProduto, '/comercio/<int:id_comercio>/categoria_produto/')
api.add_resource(Produtos, '/comercio/<int:id_comercio>/categoria_produto/<int:id_categoria>/produto/')
api.add_resource(DetalhesProduto, '/produto/<int:id_produto>/detalhes_produto/')

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
