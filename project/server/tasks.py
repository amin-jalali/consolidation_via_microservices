from celery import Celery
from project.serviceProvider.request import Request

celery = Celery('tasks', broker="redis://redis:6379", backend="redis://redis:6379")


@celery.task(name="request")
def request_handler(params):
    group = params['group']
    service_name = params['service_name']
    method = params['method']
    payload = params['payload']
    try:
        req = Request(group, service_name, method, payload)
        result = req.interact()
    except KeyError as e:
        result = str(e)

    return result

