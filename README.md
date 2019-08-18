# nuchall - Beta API - v1.0

## Setup

### Local console

- install requirements

```shell script
    python3.7 -m venv /venv \
    /venv/bin/pip install -U pip \
    /venv/bin/pip install --no-cache-dir -r /requirements.txt
```

- run application

```shell script
/venv/bin/python3 run.py
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

```jsonc
{
  "account": {
    "cardIsActive": true,
    "limit": "Number",
    "denylist": ["string"]
  },
  "lasttransactions": [
    {
      "merchant": "String",
      "amount": "Number",
      "time": "string" // 2019-08-17T11:02:00.000000
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
  "deniedReasons": [
    {
      "reason": "description of rule"
    }
  ]
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
