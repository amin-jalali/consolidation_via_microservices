from project.serviceProvider.request import Request


def test_service_provider_initiate(test_app):
    group = 'sales'
    service_name = 'products'
    method = 'GET'
    payload = ''

    assert Request(group, service_name, method, payload)
