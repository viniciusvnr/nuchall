import unittest
from datetime import datetime, timedelta
from tests.payloads import *
from services.TransactionValidator import *

payload = {
      "account": {
        "cardIsActive": True,
        "limit": 10.9,
        "denylist": []
      },
      "lasttransactions": [],
      "transaction": {
        "merchant": "loja",
        "amount": 10,
        "time": datetime.utcnow()
        # datetime(2019, 8, 17, 11, 4, 00, 000000)
      }
    }


class RuleTests(unittest.TestCase):
    def test_rule_when_amount_is_greater_then_limit_should_be_true(self):
        transaction_amount = 100
        account_limit = 90
        result = transaction_limit_rule(transaction_amount, account_limit)
        self.assertTrue(result, 'should be True')

    def test_rule_when_account_amount_is_greater_then_transaction_amount_should_be_false(self):
        transaction_amount = 100
        account_amount = 120
        result = transaction_limit_rule(transaction_amount, account_amount)
        self.assertFalse(result, 'should be False')

    def test_when_transaction_amount_is_90_percent_of_account_limit_should_be_true(self):
        transaction_amount = 90
        account_limit = 100
        result = transaction_limit90_rule(transaction_amount, account_limit)
        self.assertTrue(result, 'should be True')

    def test_when_transaction_amount_is_not_90_percent_of_account_limit_should_be_false(self):
        transaction_amount = 50
        account_limit = 100
        result = transaction_limit90_rule(transaction_amount, account_limit)
        self.assertFalse(result, 'should be false')

    def test_when_transaction_has_10_same_merchant_should_be_true(self):
        payload["transaction"]["merchant"] = "same_merchant"
        transaction_list = []
        for item in range(10):
            transaction_list.append(payload["transaction"])
        transaction_merchant = 'same_merchant'

        result = transaction_same_merchant_rule(transaction_list, transaction_merchant)
        self.assertTrue(result, 'Should be true')

    def test_when_transaction_has_10_same_merchant_should_be_false(self):
        payload["transaction"]["merchant"] = "same_merchant"
        transaction_list = []
        for item in range(10):
            transaction_list.append(payload["transaction"])
        transaction_merchant = 'diff_merchant'

        result = transaction_same_merchant_rule(transaction_list, transaction_merchant)
        self.assertFalse(result, 'Should be False')

    def test_when_transaction_is_in_deny_list_should_be_true(self):
        deny_list = ["loja10", "loja3"]
        transaction_merchant = 'loja10'
        result = transaction_deny_list_rule(transaction_merchant, deny_list)
        self.assertTrue(result, 'should be true')

    def test_when_transaction_is_in_deny_list_should_be_false(self):
        deny_list = ["loja", "loja3"]
        transaction_merchant = 'loja10'
        result = transaction_deny_list_rule(transaction_merchant, deny_list)
        self.assertFalse(result, 'should be false')

    def test_when_more_than_two_transactions_in_two_minute_interval_should_be_true(self):
        # transaction_list = transaction_limit_by_interval_rule_true_transaction_list
        transaction_list = []
        t1 = datetime(2019, 8, 17, 11, 0, 00, 000000)
        t2 = timedelta(minutes=2)
        for item in range(3):
            transaction_list.append(payload["transaction"])
            transaction_list[item]["time"] = t1 + t2
            t2 += t2

        transaction_time = datetime(2019, 8, 17, 11, 4, 00, 000000)

        result = transaction_limit_by_interval_rule(transaction_list, transaction_time)
        self.assertTrue(result, 'Should be True')

    def test_when_more_than_two_transactions_in_two_minute_interval_should_be_false(self):
        transaction_time = datetime(2019, 8, 17, 11, 8, 00, 000000)
        transaction_list = transaction_limit_by_interval_rule_false_transaction_list
        result = transaction_limit_by_interval_rule(transaction_list, transaction_time)
        self.assertFalse(result, 'Should be False')


if __name__ == '__main__':
    unittest.main()
