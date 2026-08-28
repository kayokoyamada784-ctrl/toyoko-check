import requests

URL = "https://www.toyoko-inn.com/search/result/?area=465&people=2&room=1&smoking=noSmoking&start=2026-09-19&end=2026-09-20"

response = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
)

html = response.text

print("空室なし出現回数:", html.count("空室なし"))
print("空室出現回数:", html.count("空室"))
