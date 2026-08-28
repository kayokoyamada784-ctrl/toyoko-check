import os
import requests

URL = "https://www.toyoko-inn.com/search/result/?area=465&people=2&room=1&smoking=noSmoking&start=2026-09-19&end=2026-09-20"

LINE_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_USER_ID = os.environ["LINE_USER_ID"]

response = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

html = response.text

vacancy_words = [
    "予約する",
    "空室",
    "予約可能"
]

found = any(word in html for word in vacancy_words)

if found:
    requests.post(
        "https://api.line.me/v2/bot/message/push",
        headers={
            "Authorization": f"Bearer {LINE_TOKEN}",
            "Content-Type": "application/json"
        },
        json={
            "to": LINE_USER_ID,
            "messages": [
                {
                    "type": "text",
                    "text": f"東横インに空室がある可能性があります！\n{URL}"
                }
            ]
        }
    )

    print("vacancy found")

else:
    print("no vacancy")
