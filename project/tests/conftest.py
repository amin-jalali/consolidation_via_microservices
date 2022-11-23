import pytest

from project.server import create_app


@pytest.fixture
def test_app():
    app = create_app()
    app.config.from_object("project.server.config.TestingConfig")
    with app.app_context():
        yield app
