import sqlite3
from db import db

class AccountModel(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_number = db.Column(db.String(16), unique=True)
    name = db.Column(db.String(64), nullable=True)
    unique_name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    pin = db.Column(db.Integer)
    balance = db.Column(db.Float(precision=2), default=50000.00)

    def __init__(self, phone_number, name, unique_name, email, password, pin):
        self.phone_number = phone_number
        self.name = name
        self.unique_name = unique_name
        self.email = email
        self.password = password
        self.pin = pin

    def json(self):
        return {'phone_number': self.phone_number,
                'name': self.name,
                'unique_name': self.unique_name,
                'email': self.email,
                'balance': self.balance}
    def json2(self):
        return {'phone_number': self.phone_number,
                'balance': self.balance,
                'password': self.password}

    def unique_name_json(self):
        return{'unique_name': self.unique_name}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_phone_number(cls, phone_number):
        _phone_number = phone_number
        if '+62' in phone_number:
            _phone_number = phone_number.replace('+62','0')
        return cls.query.filter_by(phone_number=_phone_number).first()

    @classmethod
    def find_by_unique_name(cls, unique_name):
        return cls.query.filter_by(unique_name=unique_name).first()

    @classmethod
    def login(cls, unique_name, password):
        return cls.query.filter_by(unique_name=unique_name, password=password).first()