# nuchall - Beta API - v1.0

## Setup

### Local

- install requirements

```sh
    python3 -m venv .venv \
    && .venv/bin/pip install -U pip \
    && .venv/bin/pip install --no-cache-dir -r requirements.txt
```

- Activate Python Virtual Env

```sh
source .venv/bin/activate
```

- run application

```sh
/venv/bin/python3 run.py
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
      "string"
    }
  ]
}
```

```http
status: 201 CREATED
```

### `Denied Reasons`

```jsonc
  "deniedReasons": [
    {
      "The transaction amount should not be above limit",
      "No transaction should be approved when the card is blocked",
      "The first transaction shouldn't be above 90% of the limit",
      "There should not be more than 10 transactions on the same merchant",
      "Merchant in deny list", // Rule 5
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
