import requests

URL = "https://www.toyoko-inn.com/search/result/?area=465&people=2&room=1&smoking=noSmoking&start=2026-09-19&end=2026-09-20"

response = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
)

html = response.text

for hotel in ["池袋", "大塚", "赤羽"]:
    pos = html.find(hotel)

    if pos != -1:
        start = max(0, pos - 300)
        end = min(len(html), pos + 1000)

        print("\n")
        print("=" * 50)
        print(hotel)
        print("=" * 50)
        print(html[start:end])
