import requests
import re

URL = "https://www.toyoko-inn.com/search/result/?area=465&people=2&room=1&smoking=noSmoking&start=2026-09-19&end=2026-09-20"

html = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
).text

for hotel in [
    "東横INN池袋北口",
    "東横INN大塚駅北口",
    "東横INN赤羽駅東口"
]:
    pos = html.find(hotel)

    print("\n")
    print("=" * 50)
    print(hotel)
    print("=" * 50)

    if pos != -1:
        print(html[pos:pos+2000])
