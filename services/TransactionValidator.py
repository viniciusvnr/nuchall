

def transaction_limit_rule(transaction):
    msg = "The transaction amount should not be above limit"
    status = transaction.amount > transaction.account_limit
    if status:
        return status, msg
    return status, None


def transaction_card_active_rule(transaction):
    msg = "No transaction should be approved when the card is blocked"
    is_active = transaction.card_is_active
    status = False
    if not is_active:
        status = True
        return status, msg
    return status, None


def transaction_limit90_rule(transaction):
    msg = "The first transaction shouldn't be above 90% of the limit"
    max_limit_percentage = 90
    trigger_limit = (transaction.account_limit * max_limit_percentage) / 100
    status = trigger_limit <= transaction.amount < transaction.account_limit
    if len(transaction.last_transactions) == 0 and status:
        return status, msg
    return status, None


def transaction_same_merchant_rule(transaction):
    msg = "There should not be more than 10 transactions on the same merchant"
    max_transactions_per_merchant = 10
    count = 0

    for trn in transaction.last_transactions:
        if trn['merchant'] == transaction.merchant:
            count += 1

    status = max_transactions_per_merchant <= count
    if status:
        return status, msg
    return status, None


def transaction_deny_list_rule(transaction):
    msg = "Merchant in deny list"
    status = transaction.merchant in transaction.deny_list
    if status:
        return status, msg
    return status, None


def transaction_limit_by_interval_rule(transaction):
    msg = "There should not be more than 3 transactions on a 2 minutes interval"
    interval_limit = 120
    transaction_trigger_limit = 3
    count = 0
    if len(transaction.last_transactions) >= 3:
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

            if abs(dt_delta) < interval_limit or abs(dt_inner_delta) < interval_limit:
                count += 1

    status = count >= transaction_trigger_limit
    if status:
        return status, msg
    return status, None


def validate_rules(transaction, rule_set):
    denied_reasons = []

    # call functions
    for r in rule_set:
        status, msg = r(transaction)
        if status and msg is not None:
            denied_reasons.append(msg)

    is_transaction_approved = len(denied_reasons) == 0

    return is_transaction_approved, denied_reasons
