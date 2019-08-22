from datetime import datetime, timedelta
from controllers.Authorize import Transaction


class TransactionHelper:
    def __init__(self):
        pass

    @classmethod
    def data_list_generator(cls, last_transactions_list_len: int, interval: float):
        cls.last_transaction_list_len = last_transactions_list_len
        cls.interval = interval

        payload = {
              "account": {
                "cardIsActive": True,
                "limit": 100,
                "denylist": []
              },
              "lasttransactions": [],
              "transaction": {
                "merchant": "loja",
                "amount": 10,
                "time": datetime.utcnow()
              }
            }

        transaction_object = Transaction(payload)
        t1 = datetime.utcnow()
        t2 = timedelta(minutes=cls.interval)

        for t in range(cls.last_transaction_list_len):
            transaction_object.last_transactions.append(
                {
                    "merchant": "loja" + str(t),
                    "amount": (t*10)/2,
                    "time": t1 - t2
                }.copy())
            t2 += t2

        return transaction_object
