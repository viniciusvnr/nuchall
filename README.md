# nuchall - Beta API - v1.0



## endpoints

| HTTP Method | URI | Action|
|------------ |-----|-------|
| GET | /api/v1.0/account | Retrieve a list of accounts  |
| GET | /api/v1.0/account/accountid | Retrieve a account |
| POST | /api/v1.0/account | create an account |
| GET | /api/v1.0/account/transaction | retrieve a list of transactions of a specified account |
| GET | /api/v1.0/account/transaction/tid | retrieve a transactions of a specified account |
| GET | /api/v1.0/merchant | Retrieve a list of merchant |
| GET | /api/v1.0/merchant/merchantid | Retrieve a list of merchant |
| POST | /api/v1.0/merchant | create a merchant |
| POST | /api/v1.0/authorize | authorize a transaction |
| GET | /api/v1.0/healthcheck | return application status |

## schema

`merchant`
```json
{
  "merchantid": "guid",
  "name" : "string",
  "enabled": true
}
```

## default schema

`account`
```json
 {
    "cardIsActive": true,
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
  "lasttransactions": [<transaction>]
}
```

`Output`
```json
{
    "approved": "Boolean", "newLimit": "Number", "deniedReasons": [ "String" ]
}
```