import os
import requests

LINE_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_USER_ID = os.environ["LINE_USER_ID"]

response = requests.post(
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
                "text": "GitHubからのテスト通知です"
            }
        ]
    }
)

print(response.status_code)
print(response.text)
