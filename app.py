from flask import Flask
from flask_restful import Api

from resources.account import AccountRegister
from resources.transfer import Transfer
from resources.ads import AdsList
from resources.topup import Topup
from resources.login import Login
from resources.getaccount import GetAccount

from application import application



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '9DEE9A16284EF3B91F35672945AEB'

#blueprints
app.register_blueprint(application)

api = Api(app)
api.add_resource(AccountRegister, '/register')
api.add_resource(Transfer, '/transfer')
api.add_resource(AdsList, '/adslist')
api.add_resource(Topup, '/topup')
api.add_resource(Login, '/login')
api.add_resource(GetAccount, '/get_uniquename_by_phone_number/<string:phone_number>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)
