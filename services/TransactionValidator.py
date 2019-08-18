from datetime import datetime


def transaction_limit_rule(transaction_amount: float, account_limit: float):
    return transaction_amount > account_limit


def transaction_limit90_rule(transaction_amount: float, account_limit: float):
    max_limit_percentage = 90
    return max_limit_percentage <= transaction_amount < account_limit


def transaction_merchant_rule(transaction_list: list):
    max_transactions_per_merchant = 10

    if transaction_list:
        count = 0

        for trn in transaction_list:
            if trn["merchant"] == transaction_list:
                count += 1

        return count >= max_transactions_per_merchant


def transaction_deny_list_rule(transaction_merchant: str, deny_list: list):
    return transaction_merchant in deny_list


def transaction_limit_by_interval_rule(transaction_list: list, current_transaction_time: datetime):
    count = 0
    for i, trn in enumerate(transaction_list):
        # timestamp da transacao da lista <latest_transactions>
        dt1 = trn["time"].timestamp()
        # timestamp da transacao do payload
        dt2 = current_transaction_time.timestamp()
        # timestamp do proximo item da lista <latest_transactions>
        idxtest = (i + 1) % len(transaction_list)
        dt2_inner = transaction_list[(i + 1) % len(transaction_list)]["time"].timestamp()
        dt_delta = dt2 - dt1
        dt_inner_delta = dt2_inner - dt1

        if dt_delta < 120.0 or dt_inner_delta < 120.0:
            count += 1

    return count >= 3


def validate_rules(input_obj):
    card_is_active = input_obj["account"]["cardIsActive"]
    account_limit = input_obj["account"]["limit"]
    deny_list = input_obj["account"]["denylist"]
    last_transactions = input_obj["lasttransactions"]
    transaction_merchant = input_obj["transaction"]["merchant"]
    transaction_amount = input_obj["transaction"]["amount"]
    transaction_time = input_obj["transaction"]["time"]
    denied_reasons = []

    # call functions
    limit_rule = transaction_limit_rule(transaction_amount, account_limit)
    merchant_rule = transaction_merchant_rule(last_transactions)
    deny_list_rule = transaction_deny_list_rule(transaction_merchant, deny_list)

    if limit_rule:
        # rule 1.
        denied_reasons.append({"reason": "The transaction amount should not be above limit"})

    if not card_is_active:
        # rule 2.
        denied_reasons.append({"reason": "No transaction should be approved when the card is blocked"})

    if len(last_transactions) == 0:
        limit_90_rule = transaction_limit90_rule(transaction_amount, account_limit)
        if limit_90_rule:
            # rule 3.
            denied_reasons.append({"reason": "The first transaction shouldn't be above 90% of the limit"})

    if merchant_rule:
        # rule 4.
        denied_reasons.append({"reason": "There should not be more than 10 transactions on the same merchant"})

    if deny_list_rule:
        # rule 5
        denied_reasons.append({"reason": "Merchant in deny list"})

    if len(last_transactions) >= 3:
        limit_by_interval_rule = transaction_limit_by_interval_rule(last_transactions, transaction_time)

        if limit_by_interval_rule:
            # rule 6
            denied_reasons.append({"reason": "There should not be more than 3 transactions on a 2 minutes interval"})

    return denied_reasons
