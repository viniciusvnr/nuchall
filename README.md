# nuchall - Beta API - v1.0

## Setup

```sh
python run.py
```

## endpoint

| HTTP Method | URI                   | Action                    |
| ----------- | --------------------- | ------------------------- |
| POST        | /api/v1.0/authorize   | authorize a transaction   |
| GET         | /api/v1.0/healthcheck | return application status |
| GET         | /api/v1.0             | Retrieve api version      |

---

## Authorize a transaction

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

## Api Version

```http
GET /api/v1.0
```

```json
{
  "version": "nuchall - Beta API - v1.0"
}
```

```http
status: 200 OK
```

## Healthcheck

```http
GET /api/v1.0/healthcheck
```

```json
{
  "isHealthy": true
}
```

```http
status: 200 OK
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
  "lasttransactions": ["{String}"]
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
