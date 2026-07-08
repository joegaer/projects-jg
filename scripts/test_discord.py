import requests
from config import DISCORD_WEBHOOK_URL

message = {"content": "Test alert from my homelab script!"}
response = requests.post(DISCORD_WEBHOOK_URL, json=message)

print("Status code:", response.status_code)