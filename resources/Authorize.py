from flask_restful import Resource

class Authorize(Resource):

    def post(self):
        return {"message": "authorize a transaction"}
