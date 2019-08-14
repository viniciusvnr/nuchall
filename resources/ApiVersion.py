from flask_restful import Resource


class GetVersion(Resource):

    def get(self):
        return {"version": "nuchall - Beta API - v1.0"}
