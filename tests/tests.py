import unittest
from datetime import datetime, timedelta
import json
import run
from controllers.Authorize import *
from services.TransactionValidator import *
from services.TransactionAuthorizationService import calculate_new_limit, authorize_transaction


def data_list_generator(last_transactions_list_len: int, interval: float):
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
    t2 = timedelta(minutes=interval)

    for t in range(last_transactions_list_len):
        transaction_object.last_transactions.append(
            {
                "merchant": "loja" + str(t),
                "amount": (t*10)/2,
                "time": t1 - t2
            }.copy())
        t2 += t2

    return transaction_object


class Tests(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = run.app
        self.client = self.app.test_client

    def test_rule_when_amount_is_greater_then_limit_should_return_true(self):
        transaction_object = data_list_generator(0, 2)
        transaction_object.amount = 100
        transaction_object.account_limit = 90
        result, msg = transaction_limit_rule(transaction_object)
        self.assertTrue(result, "should be True")
        self.assertEqual(msg, "The transaction amount should not be above limit")

    def test_rule_when_account_amount_is_greater_then_transaction_amount_should_return_false(self):
        transaction_object = data_list_generator(0, 2)
        transaction_object.amount = 100
        transaction_object.account_limit = 190
        result, msg = transaction_limit_rule(transaction_object)
        self.assertFalse(result, "should be False")
        self.assertEqual(msg, None)

    def test_when_transaction_amount_is_90_percent_of_account_limit_should_return_true(self):
        transaction_object = data_list_generator(0, 2)
        transaction_object.amount = 90
        transaction_object.account_limit = 100
        result, msg = transaction_limit90_rule(transaction_object)
        self.assertTrue(result, 'should be True')
        self.assertEqual(msg, "The first transaction shouldn't be above 90% of the limit")

    def test_when_transaction_amount_is_not_90_percent_of_account_limit_should_return_false(self):
        transaction_object = data_list_generator(0, 2)
        transaction_object.amount = 50
        transaction_object.account_limit = 100
        result, msg = transaction_limit90_rule(transaction_object)
        self.assertFalse(result, 'should be false')
        self.assertEqual(msg, None)

    def test_when_transaction_has_10_same_merchant_should_return_true(self):
        transaction_object = data_list_generator(10, 1)
        transaction_object.merchant = "same_merchant"
        for item in transaction_object.last_transactions:
            item["merchant"] = "same_merchant"

        result, msg = transaction_same_merchant_rule(transaction_object)
        self.assertTrue(result, 'Should be true')
        self.assertEqual(msg, "There should not be more than 10 transactions on the same merchant")

    def test_when_transaction_has_10_same_merchant_should_return_false(self):
        transaction_object = data_list_generator(10, 2)
        transaction_object.merchant = 'diff_merchant'

        result, msg = transaction_same_merchant_rule(transaction_object)
        self.assertFalse(result, 'Should be False')
        self.assertEqual(msg, None)

    def test_when_transaction_is_in_deny_list_should_return_true(self):
        transaction_object = data_list_generator(10, 2)
        transaction_object.deny_list = ["loja10", "loja3"]
        transaction_object.merchant = 'loja10'
        result, msg = transaction_deny_list_rule(transaction_object)
        self.assertTrue(result, 'should be true')
        self.assertEqual(msg, "Merchant in deny list")

    def test_when_transaction_is_in_deny_list_should_return_false(self):
        transaction_object = data_list_generator(10, 2)
        transaction_object.deny_list = ["loja", "loja3"]
        transaction_object.merchant = 'loja10'
        result, msg = transaction_deny_list_rule(transaction_object)
        self.assertFalse(result, 'should be false')
        self.assertEqual(msg, None)

    def test_when_more_than_two_transactions_in_two_minute_interval_should_return_true(self):
        transaction_object = data_list_generator(10, 0.5)
        result, msg = transaction_limit_by_interval_rule(transaction_object)
        self.assertTrue(result, 'Should be True')
        self.assertEqual(msg, "There should not be more than 3 transactions on a 2 minutes interval")

    def test_when_more_than_two_transactions_in_two_minute_interval_should_be_false(self):
        transaction_object = data_list_generator(10, 2.5)
        result, msg = transaction_limit_by_interval_rule(transaction_object)
        self.assertFalse(result, 'Should be False')
        self.assertEqual(msg, None)

    def test_calculate_new_limit_when_transaction_status_is_true_should_return_new_limit(self):
        transactions_status = True
        account_limit = 100
        transaction_amount = 50
        result = calculate_new_limit(transactions_status, account_limit, transaction_amount)
        self.assertEqual(result, 50)

    def test_calculate_new_limit_when_transaction_status_is_false_should_return_same_limit(self):
        transactions_status = False
        account_limit = 100
        transaction_amount = 50
        result = calculate_new_limit(transactions_status, account_limit, transaction_amount)
        self.assertEqual(result, 100)

    def test_authorize_transaction_when_transaction_is_approved(self):
        transaction_object = data_list_generator(0, 2)
        transaction_object.amount = 20
        transaction_object.account_limit = 30
        result = authorize_transaction(transaction_object)
        expected = {
              "approved": True,
              "newLimit": "{0:.2f}".format(10),
              "deniedReasons": []
         }
        self.assertEqual(result, expected)

    def test_authorize_transaction_when_transaction_is_not_approved(self):
        transaction_object = data_list_generator(0, 2)
        transaction_object.amount = 100
        transaction_object.account_limit = 30
        result = authorize_transaction(transaction_object)
        expected = {
              "approved": False,
              "newLimit": "{0:.2f}".format(30),
              "deniedReasons": ["The transaction amount should not be above limit"]
         }
        self.assertEqual(result, expected)

    def test_authorize_when_request_is_valid(self):
        payload = {
            "account": {
                "cardIsActive": True,
                "limit": 100,
                "denylist": ["loja", "loja3"]
            },
            "lasttransactions": [],
            "transaction": {
                "merchant": "loja1",
                "amount": 80,
                "time": "2019-08-18T11:03:00.000000"
            }
        }
        expected = {
            "approved": True,
            "newLimit": "20.00",
            "deniedReasons": []
        }
        res = self.client().post('/api/v1.0/authorize', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(res.json, expected)
        self.assertEqual(res.status_code, 200)

    def test_authorize_when_request_is_not_valid(self):

        payload = {
            "account": {
                "cardIsActive": True,
                "limit": "10 reais",
                "denylist": ["loja", "loja3"]
            },
            "lasttransactions": [],
            "transaction": {
                "merchant": "loja1",
                "amount": 80,
                "time": "2019-08-18T11:03:00.000000"
            }
        }
        expected = {'account': {'limit': ['Not a valid number.']}}

        res = self.client().post('/api/v1.0/authorize', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(res.json, expected)
        self.assertEqual(res.status_code, 400)


if __name__ == '__main__':
    unittest.main()
