import time

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/account_info', methods=["GET"])
def products():
    result = [{
        'name': 'Tomas',
        'age': '27',
        'account_number': '124986323352'
    }]
    time.sleep(2)
    return jsonify(result), 200


@app.route('/add_amount', methods=["POST"])
def add_product():

    time.sleep(2)
    return jsonify({'message': 'your account charged. charge: 1900$'}), 200


if __name__ == '__main__':
    app.run(port=5020, host="0.0.0.0")
