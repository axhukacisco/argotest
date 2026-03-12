from flask import Flask
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def call_c():
    logging.info("Service B calling Service C")
    r = requests.get("http://service-c:5000")
    return f"B -> {r.text}"

app.run(host="0.0.0.0", port=5000)