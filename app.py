from flask import Flask, request
from flask_restful import Api
from controllers.users import User, Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'app-ecommerce'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(User, "/users/<int:id>")
api.add_resource(Users, "/users/")

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)
