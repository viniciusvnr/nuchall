import unittest
from .TransactionHelper import TransactionHelper
from services.TransactionValidator import *


class TestTransactionValidator(unittest.TestCase):

    def test_rule_when_amount_is_greater_then_limit_should_return_true(self):
        # arrange
        transaction_object = TransactionHelper.data_list_generator(0, 2)
        transaction_object.amount = 100
        transaction_object.account_limit = 90

        # act
        result, msg = transaction_limit_rule(transaction_object)

        # assert
        self.assertTrue(result, "should be True")
        self.assertEqual(msg, "The transaction amount should not be above limit")

    def test_rule_when_account_amount_is_greater_then_transaction_amount_should_return_false(self):
        # arrange
        transaction_object = TransactionHelper.data_list_generator(0, 2)
        transaction_object.amount = 100
        transaction_object.account_limit = 190

        # act
        result, msg = transaction_limit_rule(transaction_object)

        # assert
        self.assertFalse(result, "should be False")
        self.assertEqual(msg, None)

    def test_when_transaction_amount_is_90_percent_of_account_limit_should_return_true(self):
        # arrange
        transaction_object = TransactionHelper.data_list_generator(0, 2)
        transaction_object.amount = 90
        transaction_object.account_limit = 100

        # act
        result, msg = transaction_limit90_rule(transaction_object)

        # assert
        self.assertTrue(result, 'should be True')
        self.assertEqual(msg, "The first transaction shouldn't be above 90% of the limit")

    def test_when_transaction_amount_is_not_90_percent_of_account_limit_should_return_false(self):
        # arrange
        transaction_object = TransactionHelper.data_list_generator(0, 2)
        transaction_object.amount = 50
        transaction_object.account_limit = 100

        # act
        result, msg = transaction_limit90_rule(transaction_object)

        # assert
        self.assertFalse(result, 'should be false')
        self.assertEqual(msg, None)

    def test_when_transaction_has_10_same_merchant_should_return_true(self):
        # arrange
        transaction_object = TransactionHelper.data_list_generator(10, 1)
        transaction_object.merchant = "same_merchant"
        for item in transaction_object.last_transactions:
            item["merchant"] = "same_merchant"

        # act
        result, msg = transaction_same_merchant_rule(transaction_object)

        # assert
        self.assertTrue(result, 'Should be true')
        self.assertEqual(msg, "There should not be more than 10 transactions on the same merchant")

    def test_when_transaction_has_10_same_merchant_should_return_false(self):
        # arrange
        transaction_object = TransactionHelper.data_list_generator(10, 2)
        transaction_object.merchant = 'diff_merchant'

        # act
        result, msg = transaction_same_merchant_rule(transaction_object)

        # assert
        self.assertFalse(result, 'Should be False')
        self.assertEqual(msg, None)

    def test_when_transaction_is_in_deny_list_should_return_true(self):
        # arrange
        transaction_object = TransactionHelper.data_list_generator(10, 2)
        transaction_object.deny_list = ["loja10", "loja3"]
        transaction_object.merchant = 'loja10'

        # act
        result, msg = transaction_deny_list_rule(transaction_object)

        # assert
        self.assertTrue(result, 'should be true')
        self.assertEqual(msg, "Merchant in deny list")

    def test_when_transaction_is_in_deny_list_should_return_false(self):
        # arrange
        transaction_object = TransactionHelper.data_list_generator(10, 2)
        transaction_object.deny_list = ["loja", "loja3"]
        transaction_object.merchant = 'loja10'

        # act
        result, msg = transaction_deny_list_rule(transaction_object)

        # assert
        self.assertFalse(result, 'should be false')
        self.assertEqual(msg, None)

    def test_when_more_than_two_transactions_in_two_minute_interval_should_return_true(self):
        # arrange
        transaction_object = TransactionHelper.data_list_generator(10, 0.5)

        # act
        result, msg = transaction_limit_by_interval_rule(transaction_object)

        # assert
        self.assertTrue(result, 'Should be True')
        self.assertEqual(msg, "There should not be more than 3 transactions on a 2 minutes interval")

    def test_when_more_than_two_transactions_in_two_minute_interval_should_be_false(self):
        # arrange
        transaction_object = TransactionHelper.data_list_generator(10, 2.5)

        # act
        result, msg = transaction_limit_by_interval_rule(transaction_object)

        # assert
        self.assertFalse(result, 'Should be False')
        self.assertEqual(msg, None)


if __name__ == '__main__':
    unittest.main()
