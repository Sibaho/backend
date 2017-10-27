from flask_restful import Resource, reqparse
from models.account import AccountModel
from models.notif import NotifModel
from models.history import HistoryModel
import random
import string

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

            return acc_sender.json(), 200
        elif acc_sender:
            # phone_number, name, unique_name, password, balance
            # def __init__(self, phone_number, name, unique_name, email, password, pin):
            password = self.generate_random_string()
            new_acc = AccountModel(data['phone_number_receiver'], "", data['phone_number_receiver'], "", password, "")
            new_acc.save_to_db()
            if(new_acc):
                new_acc.balance = data['amount']
                acc_sender.balance -= data['amount']

            return {'message': 'account does not exist, so system create it automatically', 'your_account': acc_sender.json(), 'account_receiver': new_acc.json2()}, 201
        else:
            return {'message': 'account not found'}

    def generate_random_string(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))