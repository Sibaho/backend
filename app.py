from flask import Flask
from flask_restful import Api

from resources.account import AccountRegister
from application import application

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'dpay'

#blueprints
app.register_blueprint(application)
api = Api(app)

api.add_resource(AccountRegister, '/daftar')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)