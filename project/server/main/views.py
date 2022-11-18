from flask import render_template, Blueprint, jsonify, request
from project.server.tasks import request_handler

main_blueprint = Blueprint("main", __name__, )


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


@main_blueprint.route("/", methods=["GET"])
def home():
    return render_template("main/home.html")


@main_blueprint.route("/request/<group>/<service_name>", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def sync_request(group, service_name):
    params = make_params(group, service_name, request)

    task = request_handler.delay((params))
    result = task.get(timeout=10)
    return jsonify({"task_result": result}), 200
