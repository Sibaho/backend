from flask_restful import Resource
from models.ads import AdsModel

class AdsList(Resource):
    def get(self):
        return {'ads': [ads.json() for ads in AdsModel.query.all()]}, 200
