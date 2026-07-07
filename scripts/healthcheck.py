import requests

HOST = "192.168.1.5"
PORT = 8081

#im adding a new line to see what happens

url = f"http://{HOST}:{PORT}"

try:
    response = requests.get(url, timeout=5)
    print("DokuWiki is UP, status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("DokuWiki is DOWN:", e)