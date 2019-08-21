from .TransactionValidator import validate_rules


def calculate_new_limit(transactions_status, account_limit, transaction_amount):

    if transactions_status:
        return account_limit - transaction_amount

    return account_limit


def is_valid_transaction(transaction):
    rule_validator = validate_rules(transaction)
    transactions_status = len(rule_validator) == 0
    return (transactions_status, rule_validator)


def authorize_transaction(transaction_object):
    transactions_status, rule_list = is_valid_transaction(transaction_object)
    account_new_limit = calculate_new_limit(
        transactions_status,
        transaction_object.account_limit,
        transaction_object.amount
        )

    return {
          "approved": transactions_status,
          "newLimit": "{0:.2f}".format(account_new_limit),
          "deniedReasons": rule_list
         }
