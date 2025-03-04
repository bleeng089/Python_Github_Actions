# Import the pytest module, which is a framework that makes it easy to write simple and scalable test cases.
import pytest

# Import the app object from the app module. 
# This is the Flask application instance that will be tested.
from app import app


# Define a pytest fixture named 'client' to create a test client for the Flask application.
@pytest.fixture
def client():
    # Use a context manager to create a test client instance of the Flask app.
    # The 'client' allows you to simulate HTTP requests to the application.
    with app.test_client() as client:
        # Yield the test client to the test function.
        yield client

# Define a test function named 'test_home' that takes the 'client' fixture as an argument.
# This function will test the home route of the Flask application.
def test_home(client):
    # Send a GET request to the root URL ("/") using the test client.
    response = client.get("/")
    # Assert that the response status code is 200 (OK).
    assert response.status_code == 200
    # Assert that the JSON response is {"status": "alive"}.
    # This checks that the home route is functioning as expected.
    assert response.json == {"status": "alive"}
