import sqlite3
from db import db

class AdsModel(db.Model):
    __tablename__ = 'ads'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.String(128))
    description = db.Column(db.String(2048))

    def __init__(self, image, description):
        self.image = image
        self.description = description

    def json(self):
        return {'id': self.id, 'image': self.image, 'description': self.description}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()