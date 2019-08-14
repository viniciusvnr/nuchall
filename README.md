# nuchall - Beta API - v1.0



## endpoints

| HTTP Method | URI | Action|
|------------ |-----|-------|
| GET | /api/v1.0/account | Retrieve a list of accounts  |
| GET | /api/v1.0/account/accountid | Retrieve a account |
| POST | /api/v1.0/account | create an account |
| GET | /api/v1.0/account/transaction | retrieve a list of transactions of a specified account |
| GET | /api/v1.0/merchant | Retrieve a list of merchant |
| GET | /api/v1.0/merchant/merchantid | Retrieve a list of merchant |
| POST | /api/v1.0/merchant | create a merchant |
| POST | /api/v1.0/authorize | authorize a transaction |
| GET | /api/v1.0/healthcheck | return application status |

## schema

`account`
```json
 {
    "cardIsActive": "Boolean",
     "limit": "Number",
     "denylist": [ "String" ]
}
```

`Transaction`
```json
{
    "merchant": "String",
     "amount": "Number",
     "time": "String"
}
```

`LastTransactions`
```json
{
  "lasttransactions": [<transactions>]
}
```

`Output`
```json
{
    "approved": "Boolean", "newLimit": "Number", "deniedReasons": [ "String" ]
}
```