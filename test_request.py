import requests

r = requests.get("https://www.google.com", timeout=30)

print(r.status_code)
