import os
import requests

webhook = os.environ["DISCORD_WEBHOOK_URL"]

requests.post(
    webhook,
    json={
        "content": "🇯🇵 Flight Tracker działa! Pierwszy test z GitHub Actions."
    },
    timeout=30,
)

print("Wysłano wiadomość na Discord.")
