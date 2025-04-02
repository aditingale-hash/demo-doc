import pytest
from app import app as flask_app # Import your Flask app instance

@pytest.fixture
def app():
  """Create a test Flask app instance."""
  yield flask_app

@pytest.fixture
def client(app):
  """Create a test client for the app."""
  return app.test_client()

def test_hello_world(client):
  """Test the '/' route."""
  response = client.get('/')
  assert response.status_code == 200
  assert b"Hello, CI/CD World!" in response.data

def test_status(client):
  """Test the '/status' route."""
  response = client.get('/status')
  assert response.status_code == 200
  assert response.data == b"OK"

# Add more tests as your application grows!