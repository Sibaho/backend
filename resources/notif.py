from flask_restful import Resource, reqparse
from models.notif import NotifModel
from models.account import AccountModel

class Notif(Resource):

    def get(self, phone_number):
        data = NotifModel.notif_true(phone_number)
        acc = AccountModel.find_by_phone_number(phone_number)
        try:
            if data and acc:
                if data.notif_status:
                    data.notif_status = False
                    data.save_to_db()
                    data.notif_status = True
                    return data.json(acc.balance)
                else:
                    return data.json(acc.balance)

        except(AttributeError, TypeError, RuntimeError, NameError):
            pass


class NotifList(Resource):
    def get(self):
        return {'notif': [ads.json2() for ads in NotifModel.query.all()]}