import os
import requests

api_key = os.environ["RAPIDAPI_KEY"]
api_host = os.environ["RAPIDAPI_HOST"]

url = "https://aerodatabox.p.rapidapi.com/airports/IATA/WAW"

headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": api_host
}

response = requests.get(url, headers=headers, timeout=30)

print("Status:", response.status_code)
print(response.text[:500])
