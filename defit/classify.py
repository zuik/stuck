import json
import requests

APP_ID = '230cac46'
APP_KEY = 'c8faffa03a6b5c782dc4dc6580c0d1e0'

OXFORD_API_ROOT = "https://od-api.oxforddictionaries.com:443/api/v1/entries/"



def define(word, language='en'):
    url = "{}{}/{}".format(OXFORD_API_ROOT,language, word.lower())
    r = requests.get(url, headers={'app_id': APP_ID, 'app_key': APP_KEY})
    if (r.status_code != 404):
        df = r.json()
        length = len(df["results"][0]["lexicalEntries"])
        string = "\n"
        for i in range(0,length):
            string = string + str(i+1) +". " +"("+df["results"][0]["lexicalEntries"][i]["lexicalCategory"]+") "+ df["results"][0]["lexicalEntries"][i]["entries"][0]["senses"][0]["definitions"][0]+"\n"
        return string
    else:
        return "404"

def synonym(word, language='en'):
    url = "{}{}/{}/{}".format(OXFORD_API_ROOT, language, word.lower(),"synonyms")
    r = requests.get(url, headers={'app_id': APP_ID, 'app_key': APP_KEY})
    if r.status_code != 404:
        df = r.json()
        arr = []
        length = len(df["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["synonyms"])
        for i in range(0, length):
            arr.append(df["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["synonyms"][i]["id"])
        string = ""
        for j in range(0, len(arr)):
            string = string + str(j + 1) + ": " + arr[j] + "\n"
        return string
    else:
        return "404"


def antonym(word, language='en'):
    url = "{}{}/{}/{}".format(OXFORD_API_ROOT, language, word.lower(), "antonyms")
    r = requests.get(url, headers={'app_id': APP_ID, 'app_key': APP_KEY})
    if r.status_code != 404:
        df = r.json()
        df = df["results"][0]["lexicalEntries"]
        atms = []
        for entry in df:
            x = [i['antonyms'] for i in entry['entries'][0]['senses']]
            for i in x:
                if len(i) > 1:
                    for j in i:
                        atms.append(j['text'])
                else:
                    atms.append(i[0]['text'])
        return "Antonyms of {}: {}".format(word, ", ".join(atms))
    else:
        return "404"

def example(word, language="en"):
    url = "{}{}/{}".format(OXFORD_API_ROOT, language, word.lower())
    r = requests.get(url, headers={'app_id': APP_ID, 'app_key': APP_KEY})
    df = r.json()
    length = len(df["results"][0]["lexicalEntries"])
    string = "\n"
    for i in range(0, length):
        string = string + str(i + 1) + ". " + df["results"][0]["lexicalEntries"][i]["entries"][0]["senses"][0]["examples"][0]["text"] + "\n"
    return string



if __name__ == "__main__":
    print(antonym("love"))
