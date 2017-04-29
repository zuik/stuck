import json
import requests

APP_ID = '230cac46'
APP_KEY = 'c8faffa03a6b5c782dc4dc6580c0d1e0'

OXFORD_API_ROOT = "https://od-api.oxforddictionaries.com:443/api/v1/entries/"


def define(word, language='en'):
    url = "{}{}/{}".format(OXFORD_API_ROOT,language, word.lower())
    r = requests.get(url, headers={'app_id': APP_ID, 'app_key': APP_KEY})
    df = r.json()
    arr =[]
    length = len(df["results"][0]["lexicalEntries"])
    for i in range(0,length):
        arr.append(df["results"][0]["lexicalEntries"][i]["entries"][0]["senses"][0]["definitions"][0])
    string = ""
    for j in range(0,len(arr)):
        string  = string + "def " + str(j+1)+ ": " + arr[j] + "\n"
    return string

#def synonym(word, language = 'en'):

<<<<<<< Updated upstream
#print(define("hypocrite"))

=======

print(define("break"))
>>>>>>> Stashed changes
