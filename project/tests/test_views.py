import json


def test_get_status(test_app):
    client = test_app.test_client()
    # fake task_id will return Pending status
    task_id = '123'

    res = client.get(f'/tasks/{task_id}'.format(task_id))
    content = json.loads(res.data.decode())

    assert content['task_status'] == "PENDING"
    assert content['task_result'] == ""
    assert content['task_id'] == task_id

    assert res.status_code == 200


def test_block_request(test_app):
    client = test_app.test_client()

    res = client.get(
        '/request/<group>/<service_name>',
        data={
            'group': 'sales',
            'service_name': 'products'
        },
        content_type='application/json'
    )

    content = json.loads(res.data.decode())
    assert res.status_code == 200
    assert content["task_result"]


def test_pool_request(test_app):
    client = test_app.test_client()
    res = client.put('/pool/<group>/<service_name>', data={
        'group': 'temp',
        'service_name': 'products'
    })
    content = json.loads(res.data.decode())
    assert res.status_code == 200
    assert content["task_id"]


def test_home(test_app):
    client = test_app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
