from flask_restful import Resource, reqparse
from models.account import AccountModel

class GetAccount(Resource):

    def get(self, phone_number):
        acc = AccountModel.find_by_phone_number(phone_number)
        if acc:
            return acc.json()
        return {'message': 'Not found'}, 404