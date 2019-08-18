from datetime import datetime


# payloads for tests
transaction_limit_by_interval_rule_false_transaction_list = [{
    "merchant": "loja",
    "amount": "10",
    "time": datetime(2019, 8, 17, 11, 4, 00, 000000)
}, {
    "merchant": "loja10",
    "amount": "20",
    "time": datetime(2019, 8, 17, 11, 6, 00, 000000)
}, {
    "merchant": "loja10",
    "amount": "25.7",
    "time": datetime(2019, 8, 17, 11, 8, 00, 000000)
}]


transaction_limit_by_interval_rule_true_transaction_list = [{
    "merchant": "loja",
    "amount": "10",
    "time": datetime(2019, 8, 17, 11, 4, 00, 000000)
}, {
    "merchant": "loja10",
    "amount": "20",
    "time": datetime(2019, 8, 17, 11, 4, 00, 000000)
}, {
    "merchant": "loja10",
    "amount": "25.7",
    "time": datetime(2019, 8, 17, 11, 4, 00, 000000)
}]


test_transaction_merchant_rule_false_list = [{
    "merchant": "loja20",
    "amount": "10",
    "time": "2019-08-17T09:41:00.000000"
}, {
    "merchant": "loja10",
    "amount": "20",
    "time": "2019-08-17T09:45:00.000000"
}]


test_transaction_merchant_rule_true_list = [{
    "merchant": "loja10",
    "amount": "10",
    "time": "2019-08-17T09:41:00.000000"
}, {
    "merchant": "loja10",
    "amount": "20",
    "time": "2019-08-17T09:45:00.000000"
}, {
    "merchant": "loja10",
    "amount": "25.7",
    "time": "2019-08-17T10:47:00.000000"
}, {
    "merchant": "loja10",
    "amount": "13.21",
    "time": "2019-08-17T11:48:00.000000"
}, {
    "merchant": "loja10",
    "amount": "7.6",
    "time": "2019-08-17T12:50:00.000000"
}, {
    "merchant": "loja10",
    "amount": "43",
    "time": "2019-08-17T13:52:00.000000"
}, {
    "merchant": "loja10",
    "amount": "100",
    "time": "2019-08-17T14:55:00.000000"
}, {
    "merchant": "loja10",
    "amount": "213.9",
    "time": "2019-08-17T15:55:00.000000"
}, {
    "merchant": "loja10",
    "amount": "17",
    "time": "2019-08-17T16:56:00.000000"
}, {
    "merchant": "loja10",
    "amount": "5.90",
    "time": "2019-08-17T16:59:00.000000"
}]
