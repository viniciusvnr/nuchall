from flask_restful import Resource


class Merchant(Resource):

    def get(self):
        return {"message": "List merchants"}

    def post(self):
        return {"message": "create new merchant"}

class GetMerchantById(Resource):
    def get(self, merchandid):
        self.merchandid = merchandid
        return {"message": "get merchant id {}".format(self.merchandid)}