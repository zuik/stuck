
import json
import requests

APP_ID = '230cac46'
APP_KEY = 'c8faffa03a6b5c782dc4dc6580c0d1e0'

OXFORD_API_ROOT = "https://od-api.oxforddictionaries.com:443/api/v1/entries/"


def define(word, language='en'):
    url = "{}{}/{}".format(OXFORD_API_ROOT,language, word.lower())
    r = requests.get(url, headers={'app_id': APP_ID, 'app_key': APP_KEY})
    df = r.json()
    dff = df["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
    return dff


print(define("hypocrite"))