

def transaction_limit_rule(transaction):
    return transaction.amount > transaction.account_limit


def transaction_limit90_rule(transaction):
    max_limit_percentage = 90
    trigger_limit = (transaction.account_limit * max_limit_percentage) / 100
    return trigger_limit <= transaction.amount < transaction.account_limit


def transaction_same_merchant_rule(transaction):
    max_transactions_per_merchant = 10
    count = 0

    for trn in transaction.last_transactions:
        if trn['merchant'] == transaction.merchant:
            count += 1

    return max_transactions_per_merchant <= count


def transaction_deny_list_rule(transaction):
    return transaction.merchant in transaction.deny_list


def transaction_limit_by_interval_rule(transaction):
    interval_limit = 120
    transaction_trigger_limit = 3
    count = 0

    for i, trn in enumerate(transaction.last_transactions):
        # timestamp da transacao da lista <latest_transactions>
        dt1 = trn["time"].timestamp()
        # timestamp da transacao do payload
        dt2 = transaction.time.timestamp()
        # timestamp do proximo item da lista <latest_transactions>
        dt2_inner = transaction.last_transactions[
            (i + 1) % len(transaction.last_transactions)]["time"].timestamp()

        dt_delta = dt2 - dt1
        dt_inner_delta = dt2_inner - dt1

        if dt_delta < interval_limit or dt_inner_delta < interval_limit:
            count += 1

    return count >= transaction_trigger_limit


def validate_rules(transaction):

    denied_reasons = []

    # call functions
    limit_rule = transaction_limit_rule(transaction)
    same_merchant_rule = transaction_same_merchant_rule(transaction)
    deny_list_rule = transaction_deny_list_rule(transaction)

    if limit_rule:
        # rule 1.
        denied_reasons.append({"reason": "The transaction amount should not be above limit"})

    if not transaction.card_is_active:
        # rule 2.
        denied_reasons.append({"reason": "No transaction should be approved when the card is blocked"})

    if len(transaction.last_transactions) == 0:
        limit_90_rule = transaction_limit90_rule(transaction)
        if limit_90_rule:
            # rule 3.
            denied_reasons.append({"reason": "The first transaction shouldn't be above 90% of the limit"})

    if transaction.last_transactions:
        if same_merchant_rule:
            # rule 4.
            denied_reasons.append({"reason": "There should not be more than 10 transactions on the same merchant"})

    if deny_list_rule:
        # rule 5
        denied_reasons.append({"reason": "Merchant in deny list"})

    if len(transaction.last_transactions) >= 3:

        limit_by_interval_rule = transaction_limit_by_interval_rule(transaction)

        if limit_by_interval_rule:
            # rule 6
            denied_reasons.append({"reason": "There should not be more than 3 transactions on a 2 minutes interval"})

    return denied_reasons
