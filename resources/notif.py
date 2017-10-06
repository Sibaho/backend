from flask_restful import Resource, reqparse
from models.notif import NotifModel

class Notif(Resource):

    def get(self, phone_number):
        data = NotifModel.notif_true(phone_number)
        try:
            if data.notif_status:
                data.notif_status = False
                data.save_to_db()
                data.notif_status = True
                return data.json()
        except(AttributeError, TypeError, RuntimeError, NameError):
            pass


class NotifList(Resource):
    def get(self):
        return {'notif': [ads.json() for ads in NotifModel.query.all()]}