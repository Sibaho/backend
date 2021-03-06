from flask_restful import Resource, reqparse
from models.account import AccountModel

class GetAccount(Resource):

    def get(self, phone_number):
        acc = AccountModel.find_by_phone_number(phone_number)
        if acc:
            return acc.json(), 200
        return {'message': 'Not found'}, 404

    def delete(self, phone_number):
        acc = AccountModel.find_by_phone_number(phone_number)
        if acc:
            acc.delete_from_db()
            return {'message': "Account deleted"}
        else:
            return {'message': 'Account not found'}