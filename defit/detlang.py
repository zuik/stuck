import json
import requests
import argparse
from google.cloud import translate

API_KEY = 'AIzaSyD7CqU__g9DvHC5J9QICO_Ltr5z38ra6BY'
DETECT = 'https://translation.googleapis.com/language/translate/v2/detect'
TRANSLATE = "https://translation.googleapis.com/language/translate/v2"
def detect_language(text):
    """Detects the text's language."""
    response = requests.post(DETECT, params={
        "q": text,
        "key": API_KEY,
    })
    if response.status_code == 200:
        result = response.json()
        return result['data']['detections'][0][0]['language']


def translate_text(target, text):
    """Translates text into the target language.
    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    response = requests.post(TRANSLATE, params={
        "q": text,
        "target": target,
        "key": API_KEY,
    })
    if response.status_code == 200:
        result = response.json()
        return result
        # translate_client = translate.Client()
        #
        # if isinstance(text, six.binary_type):
        #     text = text.decode('utf-8')
        #
        # # Text can also be a sequence of strings, in which case this method
        # # will return a sequence of results for each text.
        # result = translate_client.translate(
        #     text, target_language=target)
        #
        # print(u'Text: {}'.format(result['input']))
        # print(u'Translation: {}'.format(result['translatedText']))
        # print(u'Detected source language: {}'.format(
        #     result['detectedSourceLanguage']))


if __name__ == "__main__":
    #print(detect_language("Je suis une baguette"))
    # print(detect_language("Tên tôi là Hồ Chí "))
    #print(translate_text("en",
                         #"GitHub (exploité sous le nom de GitHub, Inc.) est un service web d'hébergement et de gestion de développement de logiciels, utilisant le logiciel de gestion de versions Git. Ce site est développé en Ruby on Rails et Erlang par Chris Wanstrath, PJ Hyett et Tom Preston-Werner. GitHub propose des comptes professionnels payants, ainsi que des comptes gratuits pour les projets de logiciels libres. Le site assure également un contrôle d'accès et des fonctionnalités destinées à la collaboration comme le suivi des bugs, les demandes de fonctionnalités, la gestion de tâches et un wiki pour chaque projet."))
