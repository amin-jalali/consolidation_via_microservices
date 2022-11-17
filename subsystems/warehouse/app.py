import time

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/get_status', methods=["GET"])
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


@app.route('/save_log', methods=["POST"])
def add_product():
    time.sleep(2)
    return jsonify({'message': 'log saved, reference code: #$#HFAK=$@@#'}), 200


if __name__ == '__main__':
    app.run(port=5030, host="0.0.0.0")
