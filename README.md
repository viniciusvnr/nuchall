# nuchall - Beta API - v1.0

## Setup

```sh
python run.py
```

## endpoint

| HTTP Method | URI                                 | Action                                                 |
| ----------- | ----------------------------------- | ------------------------------------------------------ |
| POST        | /api/v1.0/authorize                 | authorize a transaction                                |
|             |                                     |                                                        |
| GET         | /api/v1.0/version                   | Retrieve api version                                   |
| GET         | /api/v1.0/account                   | Retrieve a list of accounts                            |
| GET         | /api/v1.0/account/{accountid}       | Retrieve a account                                     |
| POST        | /api/v1.0/account                   | create an account                                      |
| GET         | /api/v1.0/account/transaction       | retrieve a list of transactions of a specified account |
| GET         | /api/v1.0/account/transaction/{tid} | retrieve a transaction of a specified account          |
| GET         | /api/v1.0/merchant                  | Retrieve a list of merchant                            |
| GET         | /api/v1.0/merchant/{merchantid}     | Retrieve a merchant                                    |
| POST        | /api/v1.0/merchant                  | create a merchant                                      |
| GET         | /api/v1.0/healthcheck               | return application status                              |

---

## Authorize a transaction

### Request

```http
POST /api/v1.0/authorize
```

### `Payload`

```json
{
  "account": {
    "cardIsActive": true,
    "limit": "Number",
    "denylist": ["merchant"]
  },
  "latesttransaction": "tid",
  "transaction": {
    "merchant": "String",
    "amount": "Number"
  }
}
```

### `Response`

```json
{
  "transaction": {
    "approved": true,
    "tid": "string",
    "merchant": "String",
    "amount": "Number",
    "time": "String"
  },
  "account": {
    "newLimit": "number"
  },
  "deniedReasons": ["String"]
}
```

```http
status: 201 CREATED
```

---

### default schema

`account`

```json
{
  "cardIsActive": true,
  "limit": "Number",
  "denylist": ["String"]
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
  "approved": "Boolean",
  "newLimit": "Number",
  "deniedReasons": ["String"]
}
```
