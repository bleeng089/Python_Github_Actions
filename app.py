"""A minimal Flask app to pass SAST and DAST checks."""

#!/usr/bin/env python3
# specifies that the Python 3 interpreter should be used to run the script.

# Import the Flask class and the jsonify function from the flask package.
# Flask is a micro web framework for Python.
# jsonify is a helper function for returning JSON responses.
from flask import Flask, jsonify

# Create an instance of the Flask class.
# __name__ is a special variable in Python that holds the name of the current module.
# Flask uses this to determine the root path for the application.
app = Flask(__name__)

# Define a route for the root URL ("/").
# @app.route is a decorator that tells Flask to call the home() function when the root URL is accessed.
# The methods parameter specifies that this route will handle only GET requests.
@app.route("/", methods=["GET"])
def home():
    """Return a basic status message."""
    # Create a JSON response with a status message.
    # jsonify converts the Python dictionary {"status": "alive"} to a JSON response.
    # The second argument, 200, is the HTTP status code for OK.
    return jsonify({"status": "alive"}), 200

# Check if the script is being run directly (as opposed to being imported as a module).
if __name__ == "__main__":
    # Run the Flask application.
    # host="0.0.0.0" makes the server accessible externally, not just on localhost.
    # port=8080 specifies the port on which the server will listen.
    # debug=False disables debug mode, which should be turned off in production for security reasons.
    app.run(host="0.0.0.0", port=8080, debug=False)
