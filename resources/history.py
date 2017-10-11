from flask_restful import Resource, reqparse
from models.history import HistoryModel

class History(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='Name transaction cannot be left blank!')
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='Price cannot be left blank!')
    parser.add_argument('qty',
                        type=int,
                        required=False)
    parser.add_argument('total',
                        type=float,
                        required=True,
                        help='Total cannot be left blank!')
    parser.add_argument('phone_number',
                        type=str,
                        required=True,
                        help='Phone number cannot be left blank!')

    def post(self):
        data = History.parser.parse_args()
        history = HistoryModel(data['name'], data['price'], data['qty'], data['total'], data['phone_number'])

        if history:
            history.status = 1
            history.save_to_db()
            return {'message': 'Transaction success', 'history': history.json()}, 201
        else:
            return{'message': 'Transaction failed'}, 400

class HistoryList(Resource):
    def get(self, phone_number):
        return {'histories': [history.json() for history in HistoryModel.find_by_phone_number(phone_number)]}, 201