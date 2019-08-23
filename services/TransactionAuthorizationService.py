from flask import current_app
from .TransactionValidator import *


def calculate_new_limit(transactions_status, account_limit, transaction_amount):
    if transactions_status:
        return account_limit - transaction_amount
    return account_limit


def authorize_transaction(transaction_object):

    # Call Rule validator
    rule_set = [
        transaction_limit_rule,
        transaction_card_active_rule,
        transaction_limit90_rule,
        transaction_same_merchant_rule,
        transaction_deny_list_rule,
        transaction_limit_by_interval_rule
    ]

    # validate_rules returns:
    # status: Bool, denied_reasons: List
    try:
        is_transaction_approved, denied_reasons_list = validate_rules(transaction_object, rule_set)
    except Exception as e:
        current_app.logger.warning(str(e))
    else:
        account_new_limit = calculate_new_limit(
            is_transaction_approved,
            transaction_object.account_limit,
            transaction_object.amount
            )

        return {
              "approved": is_transaction_approved,
              "newLimit": "{0:.2f}".format(account_new_limit),
              "deniedReasons": denied_reasons_list
             }
