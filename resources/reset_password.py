from flask_restful import Resource, reqparse
from models.account import AccountModel

class ResetPassword(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('phone_number',
                        type=str,
                        required=True,
                        help='Phone number cannot be left blank!')
    parser.add_argument('new_password',
                        type=str,
                        required=True,
                        help='Password cannot be left blank!'
                        )

    def put(self):
        data = ResetPassword.parser.parse_args()
        acc = AccountModel.find_by_phone_number(data['phone_number'])

        if acc:
            acc.password = data['new_password']
            acc.save_to_db()

            return acc.json(), 200
        else:
            return{'message': 'phone number not exist'}, 400