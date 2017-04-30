import json
import requests
import urllib

API_KEY = "53c68ea7dcab4200e1b5edc1f9f1fe71"

PRIMARY = "http://api.openweathermap.org/data/2.5/weather"

def weather(location):
    url = "{}?q={}&APPID={}".format(PRIMARY,location, API_KEY)
    response = requests.get(url)
    df = response.json()
    temp = round(df["main"]["temp"] - 273.15,2)
    return temp

def round_up(x, place):
    return round(x + 5 * 10**(-1 * (place + 1)), place)

weather("London")
