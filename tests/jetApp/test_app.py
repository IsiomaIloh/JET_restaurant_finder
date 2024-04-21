import pytest
import requests_mock
from flask import template_rendered
from contextlib import contextmanager

from app import app as flask_app


# Fixture for capturing templates used during testing
@contextmanager
def captured_templates(app):
    recorded = []   # Initializes a list to keep records of all the templates rendered.

    # This function is called whenever a template is rendered.
    def record(sender, template, context, **extra):
        recorded.append((template, context))   # We append a tuple of the template and context to our list.

    template_rendered.connect(record, app)  # Connects the record function to the template_rendered signal.
    try:
        yield recorded   # This allows us to access the list of recorded templates within the 'with' block.
    finally:
        # Once we exit the 'with' block, disconnect our function
        # so it no longer listens to the signal.
        template_rendered.disconnect(record, app)


@pytest.fixture   # This decorator tells pytest that this is a fixture.
def client():
    # Set up the configuration for the test environment.
    flask_app.config.update({
        # Enables testing mode, which can change error handling and disable certain functionalities for testing.
        "TESTING": True,
        "DEBUG": False,  # Disables debug mode for testing
    })
    # Create a test client for the application.
    with flask_app.test_client() as client:
        yield client  # 'yield' the client to the testing function. This allows tests to use the client object.


def test_home_page(client):
    """Tests the home page."""
    with captured_templates(flask_app) as templates:
        response = client.get('/')
        assert response.status_code == 200
        assert len(templates) == 1
        assert templates[0][0].name == 'index.html'


def test_get_restaurants(client):
    with requests_mock.Mocker() as m, captured_templates(flask_app) as templates:
        m.get('https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/TE11ST', json={
            "restaurants": [
                {
                    "name": "Test Restaurant",
                    "cuisines": [{"name": "Italian"}],
                    "rating": {"starRating": 4.5},
                    "address": {
                        "firstLine": "123 Test St",
                        "postalCode": "TE1 1ST",
                        "city": "Test City"
                    },
                    "logoUrl": "https://www.example.com/logo.jpg"
                }
            ]
        })
        response = client.get('/restaurants/TE11ST')
        assert response.status_code == 200

        # Confirms that a results template was rendered with the correct context
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == 'results.html'
        assert context['postcode'] == 'TE11ST'
        assert context['restaurants'][0]['name'] == 'Test Restaurant'
