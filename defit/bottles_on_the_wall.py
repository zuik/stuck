# Flask is mini-server

from flask import Flask, request


unicorn = Flask(__name__)

@unicorn.route("/")
def index():
    return "Unicorn are too sweet"

@unicorn.route("/agree")
def agree():
    r = request.args.get("name") or "No one"
    print(request.args)
    return "{} agrees that Unicorn are too sweet".format(r)


if __name__ == "__main__":
    unicorn.run(port=5001)
