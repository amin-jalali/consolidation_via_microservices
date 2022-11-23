from flask import Blueprint
from flask_swagger_ui import get_swaggerui_blueprint

from project.document.api_gateway_doc import get_local_docs
from project.serviceProvider.api_repository import apis
from project.serviceProvider.request import Request

docs_blueprint = Blueprint("docs", __name__, )


def collect_docs():
    result_set = [get_local_docs()]
    for group in apis.keys():
        group = group
        service_name = 'docs'
        method = 'GET'
        payload = ''
        try:
            req = Request(group, service_name, method, payload)
            result = req.interact()
            if result is not int:
                result_set.append(result)
        except KeyError as e:
            result = str(e)

    return result_set


def generate_swagger_doc():
    docs = collect_docs()
    paths = {}
    for doc in docs:
        for path in doc.keys():
            paths[path] = doc[path]

    result = {
        "openapi": "3.0.3",
        "info": {
            "title": "Consolidation system API documentation",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nisl suscipit adipiscing bibendum est ultricies integer. Non arcu risus quis varius quam quisque id diam vel. Congue quisque egestas diam in. Eget nulla facilisi etiam dignissim diam quis enim lobortis. Porttitor massa id neque aliquam vestibulum morbi blandit. Euismod quis viverra nibh cras pulvinar mattis nunc. Egestas congue quisque egestas diam in arcu cursus. Vestibulum lorem sed risus ultricies tristique nulla aliquet enim. Fermentum leo vel orci porta non pulvinar neque laoreet suspendisse. Faucibus nisl tincidunt eget nullam non nisi est. Tincidunt lobortis feugiat vivamus at augue eget arcu dictum varius. Eu ultrices vitae auctor eu augue ut lectus. In fermentum posuere urna nec. Lacus vel facilisis volutpat est. Varius quam quisque id diam vel quam elementum.",
            "version": "1.3.1"
        },
        "paths": paths,
        "schemes": [
            "http"
        ],
    }

    return result


SWAGGER_URL = '/api/docs'
API_URL = '/docs'
docs_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Consolidation System"
    },
)
