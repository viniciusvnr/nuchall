import json
import unittest
import run
from .TransactionHelper import TransactionHelper
from services.TransactionAuthorizationService import calculate_new_limit, authorize_transaction


class TestTransactionAuthorizationService(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = run.app
        self.client = self.app.test_client

    def test_calculate_new_limit_when_transaction_status_is_true_should_return_new_limit(self):
        # arrange
        transactions_status = True
        account_limit = 100
        transaction_amount = 50

        # act
        result = calculate_new_limit(transactions_status, account_limit, transaction_amount)

        # assert
        self.assertEqual(result, 50)

    def test_calculate_new_limit_when_transaction_status_is_false_should_return_same_limit(self):
        # arrange
        transactions_status = False
        account_limit = 100
        transaction_amount = 50

        # act
        result = calculate_new_limit(transactions_status, account_limit, transaction_amount)

        # assert
        self.assertEqual(result, 100)

    def test_authorize_transaction_when_transaction_approved_should_return_true(self):
        # arrange
        transaction_object = TransactionHelper.data_list_generator(0, 2)
        transaction_object.amount = 20
        transaction_object.account_limit = 30
        expected = {
            "approved": True,
            "newLimit": "{0:.2f}".format(10),
            "deniedReasons": []
        }

        # act
        with run.app.app_context():
            result = authorize_transaction(transaction_object)

        # assert
        self.assertEqual(result, expected)

    def test_authorize_transaction_when_transaction_approved_should_return_false(self):
        # arrange
        transaction_object = TransactionHelper.data_list_generator(0, 2)
        transaction_object.amount = 100
        transaction_object.account_limit = 30
        expected = {
            "approved": False,
            "newLimit": "{0:.2f}".format(30),
            "deniedReasons": ["The transaction amount should not be above limit"]
        }

        # act
        with run.app.app_context():
            result = authorize_transaction(transaction_object)

        # assert
        self.assertEqual(result, expected)

    def test_authorize_when_request_should_return_valid_response(self):
        # arrange
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

        # act
        res = self.client().post('/api/v1.0/authorize', data=json.dumps(payload), content_type='application/json')

        # assert
        self.assertEqual(res.json, expected)
        self.assertEqual(res.status_code, 200)

    def test_authorize_when_request_should_not_return_valid_response(self):
        # arrange
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

        # act
        res = self.client().post('/api/v1.0/authorize', data=json.dumps(payload), content_type='application/json')

        # assert
        self.assertEqual(res.json, expected)
        self.assertEqual(res.status_code, 400)
