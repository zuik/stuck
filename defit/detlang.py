import argparse
from google.cloud import translate

def detect_language(text):
    """Detects the text's language."""
    translate_client = translate.Client()

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.detect_language(text)

    print('Text: {}'.format(text))
    print('Confidence: {}'.format(result['confidence']))
    print('Language: {}'.format(result['language']))


def list_languages():
    """Lists all available languages."""
    translate_client = translate.Client()

    results = translate_client.get_languages()

    for language in results:
        print(u'{name} ({language})'.format(**language))


def list_languages_with_target(target):
    """Lists all available languages and localizes them to the target language.
    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    results = translate_client.get_languages(target_language=target)

    for language in results:
        print(u'{name} ({language})'.format(**language))
 detect_language('amie')
 