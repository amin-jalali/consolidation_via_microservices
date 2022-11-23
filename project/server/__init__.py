import os
from flask import Flask

from project.document.document import docs_blueprint
from project.server.main.views import main_blueprint


def create_app(script_info=None):
    # instantiate the app
    app = Flask(
        __name__,
        template_folder="../client/templates",
        static_folder="../client/static",
    )

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # register blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(docs_blueprint)

    # shell context for flask cli
    app.shell_context_processor({"app": app})

    return app
