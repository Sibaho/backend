import sqlite3
from db import db

class AccountModel(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_number = db.Column(db.String(16), unique=True)
    name = db.Column(db.String(64), nullable=False)
    unique_name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    pin = db.Column(db.Integer)
    balance = db.Column(db.Float(precision=2), default=0)

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

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_phone_number(cls, phone_number):
        return cls.query.filter_by(phone_number=phone_number).first()

    @classmethod
    def find_by_unique_name(cls, unique_name):
        return cls.query.filter_by(unique_name=unique_name).first()

    @classmethod
    def login(cls, unique_name, phone_number, password):
        return cls.query.filter_by(unique_name=unique_name, phone_number=phone_number, password=password).first()