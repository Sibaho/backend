from flask_restful import Resource, reqparse
from models.account import AccountModel

class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help='Email cannot be left blank!')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='Password cannot be left blank!')

    def post(self):
        data = Login.parser.parse_args()
        acc = AccountModel.login(data['email'], data['password'])

        if acc:
            return {'message': 'Login success', 'account': acc.json()}
        else:
            return{'message': 'Login failed'}