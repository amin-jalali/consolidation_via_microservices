from flask import render_template, Blueprint, jsonify, request

from project.document.document import generate_swagger_doc
from project.server.tasks import get_task_status, request_handler

main_blueprint = Blueprint("main", __name__, )


@main_blueprint.route("/", methods=["GET"])
def home():
    return render_template("main/home.html")


@main_blueprint.route("/docs", methods=["GET"])
def docs():
    return jsonify(generate_swagger_doc())


@main_blueprint.route("/tasks/<task_id>", methods=["GET"])
def get_status(task_id):
    result = get_task_status(task_id)
    return jsonify(result), 200


def make_params(group, service_name, req):
    try:
        payload = req.get_json(silent=True)
    except TypeError:
        payload = ''

    return {
        'group': group,
        'service_name': service_name,
        'method': req.method,
        'payload': payload
    }


@main_blueprint.route("/pool/<group>/<service_name>", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def pool_request(group, service_name):
    params = make_params(group, service_name, request)

    task = request_handler.delay((params))
    return jsonify({"task_id": task.id}), 200


@main_blueprint.route("/request/<group>/<service_name>", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def block_request(group, service_name):
    params = make_params(group, service_name, request)

    task = request_handler.delay((params))
    result = task.get(timeout=10)
    return jsonify({"task_result": result}), 200
