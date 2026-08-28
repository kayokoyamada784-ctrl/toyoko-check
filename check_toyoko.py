import requests
import re

URL = "https://www.toyoko-inn.com/search/result/?area=465&people=2&room=1&smoking=noSmoking&start=2026-09-19&end=2026-09-20"

html = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
).text

for word in [
    "vacancy",
    "available",
    "room",
    "空室",
    "満室",
    "reserve",
    "booking"
]:
    print(word, html.lower().count(word.lower()))
