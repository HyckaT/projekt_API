import requests
from transform_fce import *

base_url = "https://pro.openweathermap.org/data/2.5/weather?"
# api klíč v externím souboru
api_key = open("api_key", "r").read()

# nastavím konkrétní město pro zobrazení aktuálních údajů
city = "Valtice"

# výsledná url pro použití API
url = base_url+"appid="+api_key+"&q="+city

#print(url)
try:
    res = requests.get(url).json()
except:
    print("Problém s url adresou!")
#else:
#    res = requests.get(url).json()
#print(res)

# práce s JSON, který jsem z Openweather uložil do res
print("################################")
print(f"Stát: {res["sys"]["country"]}\nMěsto: {res["name"]}\nNadmořská výška: {round(feet_to_meters(res["main"]["sea_level"]),2)} m")
print(f"Teplota ve stupních Celsia: {round(kelvin_to_celsius(res["main"]["temp"]),1)}")
print(f"Rychlost větru: {res["wind"]["speed"]} km/h")
print("################################")
