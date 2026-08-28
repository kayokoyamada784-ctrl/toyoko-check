import requests
import re

URL = "https://www.toyoko-inn.com/search/result/?area=465&people=2&room=1&smoking=noSmoking&start=2026-09-19&end=2026-09-20"

html = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
).text

for m in re.finditer("vacancy", html.lower()):
    start = max(0, m.start() - 150)
    end = min(len(html), m.start() + 300)

    print("================================")
    print(html[start:end])
