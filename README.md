# Intro

This project is an example of an API that authorizes a transaction for a specific account, following some
predefined rules.


## nuchall - Beta API - v1.0

## Setup

### Local

- install requirements

```sh
    python -m venv .venv \
    && .venv/bin/pip install -U pip \
    && .venv/bin/pip install --no-cache-dir -r requirements.txt
```

- Activate Python Virtual Env

```sh
source .venv/bin/activate
```

- Tests (inside project folder)

```sh
./.venv/bin/python -m unittest tests
```

- run application

```sh
./.venv/bin/python3 run.py
```

---

### Docker

- build image

```sh
docker build -t nuchall .
```

- run container

```sh
docker run -p 5000:5000 nuchall
```

---

## Postman Collection

To help the evaluation all requests involving the rules scenarios are inside the [Postman collection file.](challenge.postman_collection.json)

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

---

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
    "amount": "Number",
    "time": "string" // 2019-08-17T11:02:00.000000
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
      "string"
    }
  ]
}
```

```http
status: 200 OK
```

### `Denied Reasons`

```jsonc
  "deniedReasons": [
    {
      "The transaction amount should not be above limit",
      "No transaction should be approved when the card is blocked",
      "The first transaction shouldn't be above 90% of the limit",
      "There should not be more than 10 transactions on the same merchant",
      "Merchant in deny list",
      "There should not be more than 3 transactions on a 2 minutes interval"
    }
```

---

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

---

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
