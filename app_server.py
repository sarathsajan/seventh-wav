from flask import Flask, render_template
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
    return render_template('index.html')