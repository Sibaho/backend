from flask_restful import Resource, reqparse
from models.account import AccountModel

class DeleteAcc(Resource):
    def delete(self, phone_number):
        acc = AccountModel.find_by_phone_number(phone_number)
        if acc:
            acc.delete_from_db()
            return {'message': "Account deleted"}
        else:
            return {'message': 'Account not found'}