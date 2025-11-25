from flask import Flask, jsonify
import datetime

# Create the Flask application instance
app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    Root route handler.

    Returns a simple HTML greeting and a link to the status endpoint.

    Returns:
        str: HTML string containing a greeting and a link to '/api/status'.
    """
    return "<p>Hello, World!</p> <br> <a href='/api/status'>Check Status</a>"

@app.route("/api/status")
def status_check():
    """
    Provide a structured status report for the API.

    Returns a JSON response with the current service status and server timestamp.

    Returns:
        flask.wrappers.Response: A Flask JSON response containing:
            - status (str): Operational status, e.g. "ok".
            - service (str): Service identifier, e.g. "flask-app-service".
            - timestamp (str): Current server time formatted as "%Y-%m-%d %H:%M:%S".
    """
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Flask's jsonify function serializes a dictionary to JSON format
    return jsonify({
        "status": "ok",
        "service": "flask-app-service",
        "timestamp": current_time
    })