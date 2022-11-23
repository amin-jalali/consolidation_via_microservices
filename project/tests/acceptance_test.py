import json

from project.serviceProvider.request import Request


def test_pool_request_flow(test_app):
    client = test_app.test_client()
    res = client.get('/pool/<group>/<service_name>', data={
        'group': 'sales',
        'service_name': 'products'
    })
    content = json.loads(res.data.decode())
    assert res.status_code == 200
    assert content["task_id"]
    task_id = content["task_id"]
    url = f'/tasks/{task_id}'.format(task_id)

    while True:
        res = client.get(url)
        assert res.status_code == 200

        content = json.loads(res.data.decode())
        assert content['task_status'] == "PENDING" or content['task_status'] == "SUCCESS"
        assert content['task_id'] == task_id

        if content['task_status'] == "SUCCESS":
            break
        else:
            assert content['task_result'] == ""


def test_request_flow():
    group = 'sales'
    service_name = 'products'
    method = 'GET'
    payload = ''

    assert Request(group, service_name, method, payload)
    req = Request(group, service_name, method, payload)
    assert type(req) == Request

    assert req.interact()
    result = req.interact()
    assert type(result) == list or type(result) == str

