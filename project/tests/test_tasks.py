import json
from unittest.mock import patch
from project.server.tasks import request_handler, get_task_status


@patch("project.server.tasks.request_handler.run")
def test_request_handler(test_app):
    params = {
        'group': 'sales',
        'service_name': 'products',
        'method': 'GET',
        'payload': '',
    }

    assert request_handler.run(params)
    request_handler.run.assert_called_once_with(params)


def test_get_task_status(test_app):
    task_id = '123'
    assert get_task_status(task_id)