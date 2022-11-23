import requests
from project.serviceProvider.api_repository import ApiRepository

api_repo = ApiRepository()


class Request:
    def __init__(self, group, service_name, method, payload):
        self.group = group
        self.service_name = service_name
        self.method = method
        self.payload = payload
        self.route = ''
        self.handler = None

        if not api_repo.validate_service(group, service_name, method):
            raise KeyError("Route .../{}/{}/ With method {} Does Not exist".format(group, service_name, method))

        self.make()

    def make(self):
        self.route = api_repo.get_url(self.group, self.service_name)
        self.handler = self.request_handler()
        return self.route

    def request_handler(self):
        if self.method == "GET":
            return requests.get
        elif self.method == "POST":
            return requests.post
        elif self.method == "PUT":
            return requests.put
        elif self.method == "DELETE":
            return requests.delete
        elif self.method == "HEAD":
            return requests.head
        elif self.method == "OPTIONS":
            return requests.options

    def interact(self):

        try:
            result = self.handler(self.route, params=self.payload)
            return result.json() if result.status_code < 400 else result.status_code
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.TooManyRedirects:
            pass
        except requests.exceptions.RequestException as e:
            pass

        return 500
