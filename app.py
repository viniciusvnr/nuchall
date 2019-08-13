from flask import Flask, jsonify, escape, request, make_response, abort
from application.objects import acc, transaction


app = Flask(__name__)

api_version = '/api/v0.1'


@app.route("/api")
def get_version():
    return 'nuchall - Beta API - v0.1'


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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
