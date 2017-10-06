from flask_restful import Resource, reqparse
from models.account import AccountModel
from models.notif import NotifModel
from models.history import HistoryModel

class Transfer(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('phone_number_sender',
                        type=str,
                        required=True,
                        help='Phone number sender cannot be left blank!')
    parser.add_argument('phone_number_receiver',
                        type=str,
                        required=True,
                        help='Phone number receiver cannot be left blank!')
    parser.add_argument('amount',
                        type=float,
                        required=True,
                        help='Amount cannot be left blank!'
                        )

    def put(self):
        data = Transfer.parser.parse_args()
        acc_sender = AccountModel.find_by_phone_number(data['phone_number_sender'])
        acc_receiver = AccountModel.find_by_phone_number(data['phone_number_receiver'])
        notif = NotifModel.notif_true(data['phone_number_receiver'])
        if acc_receiver:
            if notif:
                notif.message = "Receive balance Rp {} from {}".format(data['amount'], data['phone_number_sender'])
                notif.notif_status = True
                notif.save_to_db()
            else:
                message = "Receive balance Rp {} from {}".format(data['amount'], data['phone_number_sender'])
                new_notif = NotifModel(data['phone_number_receiver'], message, True)
                new_notif.save_to_db()

        history_sender = HistoryModel("Transfer Rp {} to {}".format(data['amount'], data['phone_number_receiver']), data['amount'], 1, data['amount'], data['phone_number_sender'])
        history_receiver = HistoryModel("Receive balance Rp {} from {}".format(data['amount'], data['phone_number_sender']), data['amount'],1, data['amount'], data['phone_number_receiver'])

        if acc_sender and acc_receiver:
            if acc_sender.balance < data['amount']:
                return {'message': 'Your balance not enough.'}


            acc_sender.balance -= data['amount']
            acc_receiver.balance += data['amount']

            acc_sender.save_to_db()
            acc_receiver.save_to_db()
            history_receiver.save_to_db()
            history_sender.save_to_db()

            return acc_sender.json()
        else:
            return{'message': 'phone number not exist'}