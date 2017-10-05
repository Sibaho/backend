import sqlite3
from db import db

class TransactionModel(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_number = db.Column(db.String(16))
    message = db.Column(db.String(256))
    notif_status = db.Column(db.Boolean)

    def __init__(self, phone_number, message, notif_status):
        self.phone_number = phone_number
        self.message = message
        self.notif_status = notif_status

    def json(self):
        return{'id': self.id, 'phone_number': self.phone_number, 'message': self.message, 'notif_status': self.notif_status}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def notif_true(cls, phone_number):
        if '+62' in phone_number:
            phone_number.replace('+62', '0')
        return cls.query.filter_by(phone_number=phone_number, notif_status=True).first()
