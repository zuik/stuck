from urllib2 import urlopen
from xml.etree import ElementTree as ET
import json
import requests

app_id = '230cac46'
app_key = 'c8faffa03a6b5c782dc4dc6580c0d1e0'

language = 'en'

##requests = urlopen("http://www.dictionaryapi.com/api/v1/references/collegiate/xml/test?key=883faa22-6561-4b2c-8525-64b8979f2953")
##requests = urlopen("https://od-api.oxforddictionaries.com/api/v1")
##response= requests.read()


##XML_understand = 

def printDEF(word_id):
    url = 'https://od-api.oxforddictionaries.com/api/v1/entries' + language + '/' + word_id.lower()
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    print("code {}\n".format(r.status_code))
    print("text \n" + r.text)
    print("json \n" + json.dumps(r.json()))


printDEF("Hypocrite")