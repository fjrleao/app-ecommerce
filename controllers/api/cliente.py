from flask import request, json
from flask_restful import Resource

users = [
    {
        "id" : 1,
        "nome" : "Fábio",
        "telefone" : "64984346505"
    },
    {
        "id" : 2,
        "nome" : "Ivairton",
        "telefone" : "66984456321"
    }
]

class User(Resource):
    def get(self, id):
        for user in users:
            if user['id'] == id:
                return user
        return {'error': 'usuário nao encontrado!'}
    
    def delete(self, id):
        if id in users:
            del user[id]
            
        return {'error': 'usuario nao encontrado'}

class Users(Resource):
    def get(self):
        clientes = ClienteModel.query.all()
        print(clientes)
        for cli in clientes:
            print(cli.nome)
        return {'ok':'ok'}
        #return users, 200

    def post(self):
        req = request.get_json()
        '''user = {
            "nome" : req['nome'],
            "telefone" : req['telefone']
        }'''
        cliente = ClienteModel(nome=req['nome'], email=req['email'])
        ClienteModel.save(cliente)
        return {'sucess' : 'usuario salvo'}

