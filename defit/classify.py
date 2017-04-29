
import json
import requests

APP_ID = '230cac46'
APP_KEY = 'c8faffa03a6b5c782dc4dc6580c0d1e0'

OXFORD_API_ROOT = "https://od-api.oxforddictionaries.com:443/api/v1/entries/"

language = 'en'


def define(word):
    url = "{}{}/{}".format(OXFORD_API_ROOT,language, word.lower())
    r = requests.get(url, headers={'app_id': APP_ID, 'app_key': APP_KEY})
    d= r.json()
    return d["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]


print(define("hypocrite"))