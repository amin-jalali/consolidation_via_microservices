import time

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/products', methods=["GET"])
def products():
    result = [{
        'name': 'iphone',
        'price': '200'
    }, {
        'name': 'samsung',
        'price': '180'
    }]
    time.sleep(2)
    return jsonify(result), 200


@app.route('/add_product', methods=["POST"])
def add_product():
    result = [{
        'name': 'iphone',
        'price': '200'
    }, {
        'name': 'samsung',
        'price': '180'
    }]
    time.sleep(2)
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(port=5010, host="0.0.0.0")
