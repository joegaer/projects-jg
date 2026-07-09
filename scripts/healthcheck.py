import requests
from datetime import datetime
from config import HOST, DISCORD_WEBHOOK_URL

services = {
    "DokuWiki": 8081,
    "Nginx Proxy Manager (Web)":8090,
    "Nginx Proxy Manager (Admin)": 8091,
    "Uptime Kuma": 3001,
    "Nagios": 9000,
    "Grafana": 3100,
    "Prometheus": 9090,
    "Node Exporter": 9100,
    "BlackBox Exporter": 9115,
}

up_count = 0
attention_count = 0
down_count = 0

for name, port in services.items():
    url = f"http://{HOST}:{port}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            result = f"{timestamp} - {name} is UP ({response.status_code})"
            up_count+= 1
        else:
            result = f"{timestamp} - {name} responded but may need attention ({response.status_code})"
            attention_count += 1
            print(result)
            requests.post(DISCORD_WEBHOOK_URL, json={"content": result})
    except requests.exceptions.RequestException as e:
        result = f"{timestamp} - {name} is DOWN: {e}"
        down_count += 1
        print(result)
        requests.post(DISCORD_WEBHOOK_URL, json={"content": result})


    with open("healthcheck.log", "a") as log_file:
            log_file.write(result + "\n")

print(f"\nSummary: {up_count} UP, {attention_count} need attention, {down_count} DOWN")
