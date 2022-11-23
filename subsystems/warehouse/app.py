import time

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/docs', methods=["GET"])
def docs():
    conf = {
        "/get_status": {
            "get": {
                "tags": [
                    "Warehouse"
                ],
                "summary": "returns status of a job",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Massa sapien faucibus et molestie ac feugiat sed lectus vestibulum. Blandit turpis cursus in hac habitasse platea dictumst quisque. Auctor augue mauris augue neque gravida in fermentum et. At risus viverra adipiscing at. Blandit massa enim nec dui nunc mattis enim ut. Eu sem integer vitae justo eget magna. Malesuada fames ac turpis egestas maecenas. Eget felis eget nunc lobortis mattis. Morbi quis commodo odio aenean sed adipiscing diam. Pretium nibh ipsum consequat nisl vel pretium lectus. Ac felis donec et odio pellentesque diam. Sapien pellentesque habitant morbi tristique senectus et netus et. Mus mauris vitae ultricies leo integer malesuada.",
                "operationId": "getProducts",
                "consumes": [
                    "application/json",
                    "application/xml"
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "parameters": [
                    {
                        "in": "body",
                        "name": "body",
                        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Massa sapien faucibus et molestie ac feugiat sed lectus vestibulum. Blandit turpis cursus in hac habitasse platea dictumst quisque. Auctor augue mauris augue neque gravida in fermentum et. At risus viverra adipiscing at. Blandit massa enim nec dui nunc mattis enim ut. Eu sem integer vitae justo eget magna. Malesuada fames ac turpis egestas maecenas. Eget felis eget nunc lobortis mattis. Morbi quis commodo odio aenean sed adipiscing diam. Pretium nibh ipsum consequat nisl vel pretium lectus. Ac felis donec et odio pellentesque diam. Sapien pellentesque habitant morbi tristique senectus et netus et. Mus mauris vitae ultricies leo integer malesuada.",
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK"
                    }
                },
            }
        },
        "/save_log": {
            "post": {
                "tags": [
                    "Warehouse"
                ],
                "summary": "save a log",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Massa sapien faucibus et molestie ac feugiat sed lectus vestibulum. Blandit turpis cursus in hac habitasse platea dictumst quisque. Auctor augue mauris augue neque gravida in fermentum et. At risus viverra adipiscing at. Blandit massa enim nec dui nunc mattis enim ut. Eu sem integer vitae justo eget magna. Malesuada fames ac turpis egestas maecenas. Eget felis eget nunc lobortis mattis. Morbi quis commodo odio aenean sed adipiscing diam. Pretium nibh ipsum consequat nisl vel pretium lectus. Ac felis donec et odio pellentesque diam. Sapien pellentesque habitant morbi tristique senectus et netus et. Mus mauris vitae ultricies leo integer malesuada.",
                "operationId": "getProducts",
                "consumes": [
                    "application/json",
                    "application/xml"
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "parameters": [
                    {
                        "in": "body",
                        "name": "body",
                        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Massa sapien faucibus et molestie ac feugiat sed lectus vestibulum. Blandit turpis cursus in hac habitasse platea dictumst quisque. Auctor augue mauris augue neque gravida in fermentum et. At risus viverra adipiscing at. Blandit massa enim nec dui nunc mattis enim ut. Eu sem integer vitae justo eget magna. Malesuada fames ac turpis egestas maecenas. Eget felis eget nunc lobortis mattis. Morbi quis commodo odio aenean sed adipiscing diam. Pretium nibh ipsum consequat nisl vel pretium lectus. Ac felis donec et odio pellentesque diam. Sapien pellentesque habitant morbi tristique senectus et netus et. Mus mauris vitae ultricies leo integer malesuada.",
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK"
                    }
                },
            }
        }
    }
    return jsonify(conf)


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
