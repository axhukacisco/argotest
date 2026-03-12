from flask import Flask
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def call_b():
    logging.info("Service A calling Service B")
    r = requests.get("http://service-b:5000")
    return f"A -> {r.text}"

app.run(host="0.0.0.0", port=5000)