from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  """Serves the homepage."""
  return 'Hello, CI/CD World!'

@app.route('/status')
def status():
  """Serves a status endpoint."""
  return 'OK', 200

if __name__ == '__main__':
  # Note: Use a proper WSGI server like Gunicorn in production
  app.run(debug=True, host='0.0.0.0', port=5000)