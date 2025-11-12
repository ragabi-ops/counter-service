#!flask/bin/python
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Separate counters
get_counter = 0
post_counter = 0


@app.route("/", methods=["GET", "POST"])
def index():
    global get_counter, post_counter

    if request.method == "POST":
        post_counter += 1
        return f"POST counter is now: {post_counter}\n"

    # GET request
    get_counter += 1
    return f"GET counter is now: {get_counter}\n"


@app.route("/healthz", methods=["GET"])
def healthz():
    """Health endpoint with both counters for visibility."""
    return jsonify(
        status="ok",
        get_counter=get_counter,
        post_counter=post_counter
    ), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 80))
    app.run(host="0.0.0.0", port=port, debug=True)
