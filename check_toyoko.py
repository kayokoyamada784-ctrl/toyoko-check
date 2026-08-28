import requests

URL = "https://www.toyoko-inn.com/search/result/?area=465&people=2&room=1&smoking=noSmoking&start=2026-09-19&end=2026-09-20"

html = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
).text

for keyword in [
    "no_vacancy",
    "vacancy",
    "availableCount",
    "remainingRooms",
    "calendar"
]:
    print("====", keyword, "====")

    pos = html.find(keyword)

    if pos != -1:
        print(html[pos:pos+500])
