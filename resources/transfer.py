from flask_restful import Resource, reqparse
from models.account import AccountModel

class Transfer(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('phone_number_sender',
                        type=str,
                        required=True,
                        help='Phone number cannot be left blank!')
    parser.add_argument('phone_number_receiver',
                        type=str,
                        required=True,
                        help='Name cannot be left blank!')
    parser.add_argument('amount',
                        type=float,
                        required=True,
                        help='Unique name cannot be left blank!'
                        )

    def put(self):
        data = Transfer.parser.parse_args()
        acc_sender = AccountModel.find_by_phone_number(data['phone_number_sender'])
        acc_receiver = AccountModel.find_by_phone_number(data['phone_number_receiver'])

        if acc_sender and acc_receiver:
            if acc_sender.balance < data['amount']:
                return {'message': 'Your balance not enough.'}

            acc_sender.balance -= data['amount']
            acc_receiver.balance += data['amount']
            acc_sender.save_to_db()
            acc_receiver.save_to_db()

            return acc_sender.json()
        else:
            return{'message': 'phone number not exist'}