from flask_restful import Resource, reqparse
from models.account import AccountModel

class AccountRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('phone_number',
                        type=str,
                        required=True,
                        help='Phone number cannot be left blank!')
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='Name cannot be left blank!')
    parser.add_argument('unique_name',
                        type=str,
                        required=True,
                        help='Unique name cannot be left blank!'
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help='Email field cannot be left blank!'
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='Password cannot be left blank!'
                        )
    parser.add_argument('pin',
                        type=int,
                        required=True,
                        help='PIN cannot be left blank!'
                        )

    def post(self):
        data = AccountRegister.parser.parse_args()

        if (AccountModel.find_by_phone_number(data['phone_number']) or AccountModel.find_by_unique_name(data['unique_name'])):
            return {'message': 'Account already exists'}, 400

        account = AccountModel(**data)
        account.save_to_db()

        return {'message': 'Account created successful'}, 201

    def get(self, phone_number):
        unique_name = AccountModel.find_by_phone_number(phone_number)
        if unique_name:
            return unique_name.unique_name_json()
        return {'message': 'Not found'}, 404