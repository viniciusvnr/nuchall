
# TODO: separar as regras em funções ??


def validate_rules(input_obj):
    card_is_active = input_obj["account"]["cardIsActive"]
    account_limit = input_obj["account"]["limit"]
    deny_list = input_obj["account"]["denylist"]
    last_transactions = input_obj["lasttransactions"]
    transaction_merchant = input_obj["transaction"]["merchant"]
    transaction_amount = input_obj["transaction"]["amount"]
    transaction_time = input_obj["transaction"]["time"]
    denied_reasons = []

    # 1. The transaction amount should not be above limit
    if transaction_amount > account_limit:
        denied_reasons.append({"rule1": "The transaction amount should not be above limit"})

    # 2. No transaction should be approved when the card is blocked
    if not card_is_active:
        denied_reasons.append({"rule2": "No transaction should be approved when the card is blocked"})

    # 3. The first transaction shouldn't be above 90% of the limit
    if transaction_amount >= (account_limit * 0.9) and len(last_transactions) == 0:
        denied_reasons.append({"rule3": "The first transaction shouldn't be above 90% of the limit"})

    # 4. There should not be more than 10 transactions on the same merchant
    if last_transactions:
        count = 0

        for trn in last_transactions:
            if trn["merchant"] == transaction_merchant:
                count += 1

        if count >= 10:
            denied_reasons.append({"rule4": "There should not be more than 10 transactions on the same merchant"})

    # 5. Merchant deny list
    if transaction_merchant in deny_list:
        denied_reasons.append({"rule5": "Merchant in deny list"})

    # 6. There should not be more than 3 transactions on a 2 minutes interval
    if len(last_transactions) >= 3:
        count = 0

        for i, trn in enumerate(last_transactions):
            # timestamp da transacao da lista <latest_transactions>
            dt1 = trn["time"].timestamp()
            # timestamp da transacao do payload
            dt2 = transaction_time.timestamp()
            # timestamp do proximo item da lista <latest_transactions>
            dt2_inner = last_transactions[(i + 1) % len(last_transactions)]["time"].timestamp()
            dt_delta = dt2 - dt1
            dt_inner_delta = dt2_inner - dt1

            if dt_delta < 120.0 or dt_inner_delta < 120.0:
                count += 1

        if count >= 3:
            denied_reasons.append({"rule6": "There should not be more than 3 transactions on a 2 minutes interval"})

    return denied_reasons
