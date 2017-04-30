from flask import Flask
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_handler():
    resp = MessagingResponse()
    resp.message("Hello, world")
    return str(resp)


@app.route("/send_sms")
def send_sms_to(number):
    number = request.args.get("number")
    TSID = ""
    TTOKEN = ""
    tclient = Client(TSID, TTOKEN)
    tclient.messages.create(to="+{}".format(number), from_="", body="")


if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
