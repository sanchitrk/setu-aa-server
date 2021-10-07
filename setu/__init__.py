import os

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def ok():
    return "ok"


@app.route("/Consent/Notification", methods=["POST"])
def consent_notification():
    print(request)
    data = request.get_json(force=True)
    print("--- data ---")
    print(data)
    return "ok"