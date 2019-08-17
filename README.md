# nuchall - Beta API - v1.0

## Setup

### Local console

- install requirements

```shell script
pip install -r requirements.txt
```

- run application

```shell script
python run.py
```

---

### Docker

- build image

```shell script
docker build -t nuchall .
```

- run container

```shell script
docker run -p 5000:5000 nuchall
```

---

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
  "lasttransactions": [
    {
      "merchant": "String",
      "amount": "Number"
    }
  ],
  "transaction": {
    "merchant": "String",
    "amount": "Number"
  }
}
```

### `Response`

```json
{
  "approved": "Boolean",
  "newLimit": "Number",
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
  "lasttransactions": ["String"]
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
