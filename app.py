from flask import Flask, jsonify, escape, request, make_response, abort
from application.objects import acc, transaction, transactions
from datetime import datetime


app = Flask(__name__)

api_version = '/api/v1.0'


@app.route("/api")
def get_version():
    return 'nuchall - Beta API - v1.0'


@app.route(api_version + '/account', methods=['GET', 'POST'])
def account():
    if request.method == 'GET':
        if len(acc) == 0:
            abort(404)
        return jsonify({"accounts": acc})

    if request.method == 'POST':
        if not request.json:
            abort(400)

        new_acc = {
                "account_id": acc[-1]['account_id'] + 1,
                "cardIsActive": request.json["cardIsActive"],
                "limit": request.json["limit"],
                "denylist": request.json["denylist"]
                }
        acc.append(new_acc)
        return jsonify({"account": new_acc}), 201


@app.route(api_version + "/account/<int:account_id>")
def get_account(account_id):
    account = [ac for ac in acc if ac["account_id"] == account_id]
    if len(account) == 0:
        abort(404)
    return jsonify({"account": account[0]})


@app.route(api_version + "/authorize", methods=['POST'])
def authorize():
    date_time = datetime.utcnow()
    tr_date = date_time.strftime('%Y-%m-%d %H:%M:%S')

    tr = [{
        "merchant": request.json["merchant"],
        "amount": request.json["amount"],
        "time": tr_date
        }]

    transactions.append(tr)

    return jsonify({"transactions": tr}), 201


@app.route(api_version + "/transactions")
def get_transactions():
    if len(transactions) == 0:
        abort(404)
    return jsonify({"transactions": transactions})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
