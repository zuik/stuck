from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

TSID = "ACd3d6e4fed0307c74bd8db2d07d9f4e3b"
TTOKEN = "5d19e13da333c40b5919746f06169ecd"

tclient = Client(TSID, TTOKEN)

@app.route("/sms")
def sms_handler():
    msg = request.args.get("msg")

