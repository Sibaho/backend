import sqlite3
import datetime
from db import db

class HistoryModel(db.Model):
    __tablename__ = 'history'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Float(precision=2))
    qty = db.Column(db.Integer, default=1)
    total = db.Column(db.Float(precision=2))
    status = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    account_phonenumber = db.Column(db.Integer, db.ForeignKey('accounts.phone_number'))
    account = db.relationship('AccountModel', foreign_keys=[account_phonenumber])

    def __init__(self, name, price, qty, total, account_phonenumber):
        self.name = name
        self.price = price
        self.qty = qty
        self.total = total
        self.account_phonenumber = account_phonenumber

    def json(self):
        return{'id': self.id, 'name': self.name, 'price': self.price, 'qty': self.qty, 'total': self.total, 'status': self.status, 'phone_number': self.account_phonenumber}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_phone_number(cls, phone_number):
        return cls.query.filter_by(account_phonenumber=phone_number).all()
