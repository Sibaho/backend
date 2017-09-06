from flask_restful import Resource, reqparse
from models.account import AccountModel

class Topup(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('phone_number',
                        type=str,
                        required=True,
                        help='Phone number cannot be left blank!')
    parser.add_argument('amount',
                        type=float,
                        required=True,
                        help='Amount cannot be left blank!'
                        )

    def put(self):
        data = Topup.parser.parse_args()
        acc = AccountModel.find_by_phone_number(data['phone_number'])

        if acc:
            acc.balance += data['amount']
            acc.save_to_db()

            return acc.json()
        else:
            return{'message': 'phone number not exist'}