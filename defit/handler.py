import json
from flask import Flask, request, Response
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse

from classify import define, antonym, synonym, example
from yelp import ssearch
from weather import weather, set_risef
from detlang import detect_language, translate_text
app = Flask(__name__)

TSID = "ACd3d6e4fed0307c74bd8db2d07d9f4e3b"
TTOKEN = "5d19e13da333c40b5919746f06169ecd"

tclient = Client(TSID, TTOKEN)


@app.route("/sms", methods=['GET', 'POST'])
def sms_handler():
    print(request.form)
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
            resp.message("{}: {}".format(words, df))
        return str(resp)
    elif (msg.split(" ")[0]).lower() == ('pronounce'):
        words = msg.split(" ")[1]
        call = tclient.api.account.calls.create(to=fr_num, from_="+19712703263", url="https://ear-tube-zkn.c9users.io/say?words={}".format(words))
        return str(call.sid)
    elif msg.split(" ")[0].lower() == 'synonym':
        words = msg.split(" ")[1:]
        words = " ".join(words)
        symn = synonym(words)
        if(symn == '404'):
            errormsg = 'Check for typos'
            resp = MessagingResponse()
            resp.message(errormsg)
        else:
            resp = MessagingResponse()
            resp.message(symn)
        return str(resp)
    elif msg.split(" ")[0].lower() == 'antonym':
        words = msg.split(" ")[1:]
        words = " ".join(words)
        antm = antonym(words)
        if(antm == '404'):
            errormsg = 'Check for typos'
            resp = MessagingResponse()
            resp.message(errormsg)
        else:
            resp = MessagingResponse()
            resp.message(antm)
        return str(resp)
    elif msg.split(" ")[0].lower() == 'example':
        words = msg.split(" ")[1:]
        words = " ".join(words)
        ex = example(words)
        if(ex == '404'):
            errormsg = 'Check for typos'
            resp = MessagingResponse()
            resp.message(errormsg)
        else:
            resp = MessagingResponse()
            resp.message(ex)
        return str(resp)
    elif msg.split(" ")[0].lower() == 'food':
        words = msg.split(" ")[1:]
        yelpper = ssearch(words[0], " ".join(words[1:]))
        resp = MessagingResponse()
        resp.message(yelpper)
        return str(resp)
    elif msg.split(" ")[0].lower() == 'unicorn':
        resp = MessagingResponse()
        resp.message("GitHub (exploité sous le nom de GitHub, Inc.) est un service web d'hébergement et de gestion de développement de logiciels, utilisant le logiciel de gestion de versions Git. Ce site est développé en Ruby on Rails et Erlang par Chris Wanstrath, PJ Hyett et Tom Preston-Werner. GitHub propose des comptes professionnels payants, ainsi que des comptes gratuits pour les projets de logiciels libres. Le site assure également un contrôle d'accès et des fonctionnalités destinées à la collaboration comme le suivi des bugs, les demandes de fonctionnalités, la gestion de tâches et un wiki pour chaque projet.")
        return str(resp)
    elif msg.split(" ")[0].lower() == 'weather':
        words = msg.split(" ")[1:]
        words = " ".join(words)
        w = weather(words)
        resp = MessagingResponse()
        resp.message(w)
        return str(resp)
    elif msg.split(" ")[0].lower() == 'sunset':
        words = msg.split(" ")[1:]
        words = " ".join(words)
        w = set_rise(words,"sunset")
        resp = MessagingResponse()
        resp.message(w)
        return str(resp)
    elif msg.split(" ")[0].lower() == 'sunrise':
        words = msg.split(" ")[1:]
        words = " ".join(words)
        w = set_rise(words,"sunrise")
        resp = MessagingResponse()
        resp.message(w)
        return str(resp)
    elif msg.split(" ")[0].lower() == 'detect':
        words = msg.split(" ")[1:]
        words = " ".join(words)
        w = detect_language(words)
        resp = MessagingResponse()
        resp.message(w)
        return str(resp)
    elif msg.split(" ")[0].lower() == 'translate':
        words = msg.split(" ")[1:]
        words = " ".join(words)
        w = translate_text('en', words)
        resp = MessagingResponse()
        resp.message(w)
        return str(resp)
    else:
        greeting = "Options on Stuck\n"
        options = "DICTIONARY\n1) Definition: define name_of_word\n 2) Pronounciation: pronounce name_of_word\n3) Synonyms: synonym name_of_word\n4) Antonyms: antonym name_of_word\n5) Example sentence: example name_of_word\n"
        mo_options = "FOOD SUGGESTIONS\nfood name_of_food area\nExample: \nfood tacos Boston,MA"
        resp = MessagingResponse()
        resp.message(greeting + options + mo_options)

# import sys
# from io import StringIO
# import contextlib

# @contextlib.contextmanager
# def stdoutIO(stdout=None):
#     old = sys.stdout
#     if stdout is None:
#         stdout = StringIO()
#     sys.stdout = stdout
#     yield stdout
#     sys.stdout = old

# @app.route("/code", methods=['GET', 'POST'])
# def code():
#     msg = request.form['Body']
#     fr_num = request.form['From']
#     resp = MessagingResponse()
#     r = ""
#     with stdoutIO() as s:
#         exec(msg)
#         r = s.getvalue()
#     resp.message(r)
#     print(resp)
#     return str(resp)
    


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

