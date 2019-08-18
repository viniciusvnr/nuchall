from .TransactionValidator import validate_rules


def calculate_new_limit(transactions_status, account_limit, transaction_amount):

    if transactions_status:
        return account_limit - transaction_amount

    return account_limit


def authorize_transaction(authorization_request):
    # Call Rule validator
    val_rules = validate_rules(authorization_request)
    account_limit = authorization_request["account"]["limit"]
    transaction_amount = authorization_request["transaction"]["amount"]
    transactions_status = len(val_rules) == 0
    account_new_limit = calculate_new_limit(transactions_status, account_limit, transaction_amount)

    return {
          "approved": transactions_status,
          "newLimit": account_new_limit,
          "deniedReasons": val_rules
         }
