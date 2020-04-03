from flask import Flask, request
from flask_restful import Api
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models.estado import Estado, Cidade
from controllers.web.cliente import hello_page
from controllers.api.cliente import User, Users

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

#rotas da API
api.add_resource(User, "/users/<int:id>")
api.add_resource(Users, "/users/")

#rotas da aplicaçao web
app.register_blueprint(hello_page)

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
