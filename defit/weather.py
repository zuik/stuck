import json
import requests

API_KEY = "53c68ea7dcab4200e1b5edc1f9f1fe71"

PRIMARY = "http://api.openweathermap.org/data/2.5/weather"

def weather(location):
    url = "{}?q={}&APPID={}".format(PRIMARY,location, API_KEY)
    response = requests.get(url)
    df = response.json()
    temp = round(df["main"]["temp"] - 273.15,2)
    return "Current temperature in {} is {} degrees C".format(location, temp)

def round_up(x, place):
    return round(x + 5 * 10**(-1 * (place + 1)), place)

def set_rise(location, what):
    url = "{}?q={}&APPID={}".format(PRIMARY, location, API_KEY)
    response = requests.get(url)
    df = response.json()
    long=df["coord"]["lon"]
    lati=df["coord"]["lat"]
    url_sun = "https://api.sunrise-sunset.org/json?lat={}&lng={}".format(str(lati),str(long))
    response_sun = requests.get(url_sun)
    dff = response_sun.json()
    if(what == "sunset"):
        return dff["results"]["sunset"]
    else:
        return dff["results"]["sunrise"]

weather("London")
print(set_rise("Boston","sunset"))