acc = [{
    "account_id": 1,
    "cardIsActive": False,
    "limit": 1500.8,
    "denylist": [
                "String"
                ]
}]
transaction = {
    "merchant": "String",
    "amount": "Number",
    "time": "String"
}

# `LastTransactions` [ <Transaction> ]

#
# output = {
#     "approved": "Boolean",
#     "newLimit": "Number",
#     "deniedReasons": [
#                      "String"
#                      ]
# }