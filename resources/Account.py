from flask_restful import Resource


class Account(Resource):

    def get(self):
        return {"message": "get account"}

    def post(self):
        return {"message": "create account"}


class AccountById(Resource):

    def get(self, accountid):
        self.accountid = accountid
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