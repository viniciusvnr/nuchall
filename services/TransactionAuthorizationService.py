from .TransactionValidator import validate_rules


def authorize_transaction(authorization_request):
    # Call Rule validator
    val_rules = validate_rules(authorization_request)
    account_limit = authorization_request["account"]["limit"]
    transaction_amount = authorization_request["transaction"]["amount"]
    transactions_status = len(val_rules) == 0

    if transactions_status:
        account_new_limit = account_limit - transaction_amount
    else:
        account_new_limit = account_limit

    return {
          "approved": transactions_status,
          "newLimit": account_new_limit,
          "deniedReasons": val_rules
         }
