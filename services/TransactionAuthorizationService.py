from .TransactionValidator import validate_rules


def calculate_new_limit(transactions_status, account_limit, transaction_amount):

    if transactions_status:
        return account_limit - transaction_amount

    return account_limit


def authorize_transaction(transaction_object):
    # Call Rule validator
    val_rules = validate_rules(transaction_object)

    transactions_status = len(val_rules) == 0

    account_new_limit = calculate_new_limit(
        transactions_status,
        transaction_object.account_limit,
        transaction_object.amount
        )

    return {
          "approved": transactions_status,
          "newLimit": "{0:.2f}".format(account_new_limit),
          "deniedReasons": val_rules
         }
