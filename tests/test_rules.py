import unittest
from tests.payloads import *
from services.TransactionValidator import *


# TODO: Unit Tests


class RuleTests(unittest.TestCase):
    def test_limit_rule_true(self):
        transaction_amount = 100
        account_amount = 90
        result = transaction_limit_rule(transaction_amount, account_amount)
        self.assertTrue(result, 'should be True')

    def test_transaction_limit_rule_false(self):
        transaction_amount = 100
        account_amount = 120
        result = transaction_limit_rule(transaction_amount, account_amount)
        self.assertFalse(result, 'should be False')

    def test_transaction_limit_90_rule_true(self):
        transaction_amount = 90
        account_limit = 100
        result = transaction_limit90_rule(transaction_amount, account_limit)
        self.assertTrue(result, 'should be True')

    def test_transaction_limit_90_rule_false(self):
        transaction_amount = 50
        account_limit = 100
        result = transaction_limit90_rule(transaction_amount, account_limit)
        self.assertFalse(result, 'should be false')

    def test_transaction_merchant_rule_true(self):
        transaction_list = test_transaction_merchant_rule_true_list
        transaction_merchant = 'loja10'
        result = transaction_merchant_rule(transaction_list, transaction_merchant)
        self.assertTrue(result, 'Should be true')

    def test_transaction_merchant_rule_false(self):
        transaction_list = test_transaction_merchant_rule_false_list
        transaction_merchant = 'loja10'
        result = transaction_merchant_rule(transaction_list, transaction_merchant)
        self.assertFalse(result, 'Should be False')

    def test_transaction_deny_list_rule_true(self):
        deny_list = ["loja10", "loja3"]
        transaction_merchant = 'loja10'
        result = transaction_deny_list_rule(transaction_merchant, deny_list)
        self.assertTrue(result, 'should be true')

    def test_transaction_limit_by_interval_rule_true(self):
        transaction_time = datetime(2019, 8, 17, 11, 4, 00, 000000)
        transaction_list = transaction_limit_by_interval_rule_true_transaction_list
        result = transaction_limit_by_interval_rule(transaction_list, transaction_time)
        self.assertTrue(result, 'Should be True')

    def test_transaction_limit_by_interval_rule_false(self):
        transaction_time = datetime(2019, 8, 17, 11, 8, 00, 000000)
        transaction_list = transaction_limit_by_interval_rule_false_transaction_list
        result = transaction_limit_by_interval_rule(transaction_list, transaction_time)
        self.assertFalse(result, 'Should be False')


if __name__ == '__main__':
    unittest.main()
