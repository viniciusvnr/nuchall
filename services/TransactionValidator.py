from datetime import datetime
# Rules
# 1. The transaction amount should not be above limit
# 2. No transaction should be approved when the card is blocked
# 3. The first transaction shouldn't be above 90% of the limit
# 4. There should not be more than 10 transactions on the same merchant
# 5. Merchant deny list
# 6. There should not be more than 3 transactions on a 2 minutes interval

"""
output = {
              "approved": "Boolean",
              "newLimit": "Number",
              "deniedReasons": ["String"],
             }
"""


def validate_rules(input_obj):
    card_is_active = input_obj["account"]["cardIsActive"]
    account_limit = input_obj["account"]["limit"]
    deny_list = input_obj["account"]["denylist"]
    latest_transactions = input_obj["latesttransactions"]
    transaction_merchant = input_obj["transaction"]["merchant"]
    transaction_amount = input_obj["transaction"]["amount"]
    transaction_time = input_obj["transaction"]["time"]
    denied_reasons = []

    if transaction_amount > account_limit:
        denied_reasons.append({"rule1": "The transaction amount should not be above limit"})

    if not card_is_active:
        denied_reasons.append({"rule2": "No transaction should be approved when the card is blocked"})

    if transaction_amount >= (account_limit * 0.9) and len(latest_transactions) == 0:
        denied_reasons.append({"rule3": "The first transaction shouldn't be above 90% of the limit"})

    if latest_transactions:
        count = 0

        for trn in latest_transactions:
            if trn["merchant"] == transaction_merchant:
                count += 1

        if count >= 10:
            denied_reasons.append({"rule4": "There should not be more than 10 transactions on the same merchant"})

    if transaction_merchant in deny_list:
        denied_reasons.append({"rule5": "Merchant in deny list"})

    if len(latest_transactions) >= 3:
        count = 0

        for i, trn in enumerate(latest_transactions):
            # timestamp da transacao da lista <latest_transactions>
            dt1 = trn["time"].timestamp()
            # timestamp da transacao do payload
            dt2 = transaction_time.timestamp()
            # timestamp do proximo item da lista <latest_transactions>
            dt2_inner = latest_transactions[(i + 1) % len(latest_transactions)]["time"].timestamp()
            dt_delta = dt2 - dt1
            dt_inner_delta = dt2_inner - dt1

            if dt_delta < 120.0 or dt_inner_delta < 120.0:
                count += 1

        if count >= 3:
            denied_reasons.append({"rule6": "There should not be more than 3 transactions on a 2 minutes interval"})

    return denied_reasons

