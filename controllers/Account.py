from flask_restful import Resource, request

# validacao do request
class Account(Resource):
    def get(self):
        return {"message": "get account"}

    def post(self):
        return {"message": "create account"}, 201


class AccountById(Resource):
    def get(self, accountid):
        # Validacao e deserializacao

        self.accountid = accountid

        # TODO:  Chamada pra servico
        # response = accountService.processaChamada(accountid)

        # Preparo do retorno

        return {"message": "get account by id {}".format(self.accountid)}


class GetTransactions(Resource):
    def get(self, accountid):
        self.accountid = accountid
        return {"message": "List transactions"}


class GetTransactionById(Resource):
    def get(self, accountid, tid):
        self.accountid = accountid
        self.tid = tid
        return {"message": "List transaction by tid {}".format(self.tid)}
