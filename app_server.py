from flask import Flask, jsonify
import datetime

# Create the Flask application instance
app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    The root route handler. Returns a simple "Hello, World!" message.
    """
    return "<p>Hello, World!</p> <br> <a href='/api/status'>Check Status</a>"

@app.route("/api/status")
def status_check():
    """
    A new route to provide a structured status check (common for APIs).
    It returns a JSON object with the current time and status.
    """
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Flask's jsonify function serializes a dictionary to JSON format
    return jsonify({
        "status": "ok",
        "service": "flask-app-service",
        "timestamp": current_time
    })