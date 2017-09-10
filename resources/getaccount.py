from flask_restful import Resource, reqparse
from models.account import AccountModel

class GetAccount(Resource):

    def get(self, phone_number):
        unique_name = AccountModel.find_by_phone_number(phone_number)
        if unique_name:
            return unique_name.unique_name_json()
        return {'message': 'Not found'}, 404