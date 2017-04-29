from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

TSID = "ACd3d6e4fed0307c74bd8db2d07d9f4e3b"
TTOKEN = "5d19e13da333c40b5919746f06169ecd"

tclient = Client(TSID, TTOKEN)

@app.route("/sms", methods=['POST'])
def sms_handler():
    msg = request.form['Body']
    fr_num = request.form['From']
    if msg.split(" ")[0] == 'define':
        words = msg.split(" ")[1:]
        words = " ".join(words)
        resp = MessagingResponse()
        resp.message("You want to define: {}".format(words))
    return str(resp)

@app.route("/")
def index():
    return "Hello, world"

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")

# @app.route("/sms")
# def sms_handler():
#     msg = request.args.get("msg")

