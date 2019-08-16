import uuid
from flask import request

# TODO: implementar regras
# 1. The transaction amount should not be above limit
# 2. No transaction should be approved when the card is blocked
# 3. The first transaction shouldn't be above 90% of the limit
# 4. There should not be more than 10 transactions on the same merchant
# 5. Merchant denylist
# 6. There should not be more than 3 transactions on a 2 minutes interval


# TODO: retornar tid no output = uuid
# uuid.uuid4()

def authorize_transaction():
    output = {
              "approved": "Boolean",
              "newLimit": "Number",
              "deniedReasons": ["String"]
             }
    return output
