import requests

URL = "https://www.toyoko-inn.com/search/result/?area=465&people=2&room=1&smoking=noSmoking&start=2026-09-19&end=2026-09-20"

response = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
)

html = response.text

print("満室:", "満室" in html)
print("空室:", "空室" in html)
print("予約可能:", "予約可能" in html)
print("予約する:", "予約する" in html)
print("空室なし:", "空室なし" in html)
