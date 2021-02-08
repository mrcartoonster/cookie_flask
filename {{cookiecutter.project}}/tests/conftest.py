# -*- coding: utf-8 -*-
import pytest
from main import create_app


@pytest.fixture(scope="module")
def client():
    """
    Flask app instance with Test config.

    Fixture will be called client. Same as the function name.

    """
    flask_app = create_app()
    flask_app.config.from_object("config.TestConfig")

    # Create a test client using the Flask application configured for testing.
    with flask_app.test_client() as testing_client:
        # Establish the application context.
        with flask_app.app_context():
            yield testing_client
