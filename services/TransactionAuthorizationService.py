from .TransactionValidator import validate_rules


def authorize_transaction(authorization_request):
    # Call Rule validator
    val_rules = validate_rules(authorization_request)
    account_limit = authorization_request["account"]["limit"]
    transaction_amount = authorization_request["transaction"]["amount"]
    account_new_limit = account_limit - transaction_amount

    if val_rules:
        return {
              "approved": False,
              "newLimit": account_limit,
              "deniedReasons": val_rules
             }
    else:
        return {
              "approved": True,
              "newLimit": account_new_limit,
              "deniedReasons": val_rules
             }
