from flask_restful import Resource


class Authorize(Resource):

    def post(self):
        # TODO: validação do payload.
        # TODO: chamada para o serviço de authorização

        return {"message": "authorize a transaction"}, 201
