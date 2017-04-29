import json
from flask import Flask, request, Response
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse

from classify import define, antonym

app = Flask(__name__)

TSID = "ACd3d6e4fed0307c74bd8db2d07d9f4e3b"
TTOKEN = "5d19e13da333c40b5919746f06169ecd"

tclient = Client(TSID, TTOKEN)

@app.route("/sms", methods=['GET','POST'])
def sms_handler():
    msg = request.form['Body']
    fr_num = request.form['From']
    print(request.form)
    if msg.split(" ")[0].lower() == 'define':
        words = msg.split(" ")[1:]
        words = " ".join(words)
        df = define(words)
        if(df == '404'):
            errormsg = 'Check for typos'
            resp = MessagingResponse()
            resp.message("{}: {}".format(words, errormsg))
        else:
            pos = ""
            resp = MessagingResponse()
            resp.message("{} ({}): {}".format(words, pos, df))
        return str(resp)
    elif (msg.split(" ")[0]).lower() == ('pronounce'):
        words = msg.split(" ")[1]
        call = tclient.api.account.calls.create(to=fr_num, from_="+19712703263", url="https://ear-tube-zkn.c9users.io/say?words={}".format(words))
        return str(call.sid)
    elif msg.split(" ")[0].lower() == 'synonym':
        # code for synonym
        pass
    elif msg.split(" ")[0].lower() == 'antonym':
        words = msg.split(" ")[1:]
        words = " ".join(words)
        antm = antonym(words)
        resp = MessagingResponse()
        resp.message(antm)
        return str(resp)
    elif msg.split(" ")[0].lower() == 'example':
        pass
    return "Hlah"

@app.route("/say", methods=['GET', 'POST'])
def say():
    words = request.args.get("words")
    resp = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say voice="alice" language="en-US">The word is pronounced {}. Repeat: {}. {}</Say>
</Response>""".format(words, words, words)
    print(resp)
    return Response(resp, mimetype="text/xml")

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")

# @app.route("/sms")
# def sms_handler():
#     msg = request.args.get("msg")

