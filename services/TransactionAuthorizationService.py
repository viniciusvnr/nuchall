import uuid

# TODO: implementar regras
# 1. The transaction amount should not be above limit
# 2. No transaction should be approved when the card is blocked
# 3. The first transaction shouldn't be above 90% of the limit
# 4. There should not be more than 10 transactions on the same merchant
# 5. Merchant denylist
# 6. There should not be more than 3 transactions on a 2 minutes interval

"""
output = {
              "approved": "Boolean",
              "newLimit": "Number",
              "deniedReasons": ["String"]
             }
"""

# TODO: retornar tid no output = uuid
# uuid.uuid4()


def authorize_transaction(input_obj):
    cardisactive = input_obj["account"]["cardIsActive"]
    limit = input_obj["account"]["limit"]
    denylist = input_obj["account"]["denylist"]
    latesttransaction = input_obj["latesttransaction"]
    trn_merchant = input_obj["transaction"]["merchant"]
    trn_amount = input_obj["transaction"]["amount"]

    # test
    transactions = [{"merchant": "loja2", "amount": "89"}]

    if trn_amount > limit:
        return {"rule1": "The transaction amount should not be above limit"}
    elif not cardisactive:
        return {"rule2": "No transaction should be approved when the card is blocked"}
    elif trn_amount >= (limit * 0.9) and len(transactions) == 1:
        return {"rule3": "The first transaction shouldn't be above 90% of the limit"}
    elif transactions:
        count = 0
        for t in transactions:
            if t["merchant"] == trn_merchant:
                count += 1
        if count >= 10:
            return {"rule4": "There should not be more than 10 transactions on the same merchant"}
    if trn_merchant in denylist:
        return {"rule5": "Merchant in denylist"}

    return {"message": "foi"}
