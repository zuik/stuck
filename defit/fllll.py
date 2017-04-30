from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

TSID = "ACd3d6e4fed0307c74bd8db2d07d9f4e3b"
TTOKEN = "5d19e13da333c40b5919746f06169ecd"

@app.route("/sms", methods=['GET', 'POST'])
def sms_handler():
    resp = MessagingResponse()
    resp.message("Hello, world")
    return str(resp)


@app.route("/send_sms")
def send_sms_to():
    number = request.args.get("number")
    msg = request.args.get("msg") or ""
    tclient = Client(TSID, TTOKEN)
    tclient.messages.create(to="+{}".format(number), from_="+19712703263", body=msg)
    return str("Done")


if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
