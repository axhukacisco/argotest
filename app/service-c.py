from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def hello():
    logging.info("Service C responding")
    return "Hello from C"

app.run(host="0.0.0.0", port=5000)