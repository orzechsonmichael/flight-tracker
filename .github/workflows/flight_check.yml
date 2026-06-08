import os
import requests

api_key = os.environ["RAPIDAPI_KEY"]

url = "https://google-flights2.p.rapidapi.com/api/v1/searchFlights"

querystring = {
    "departure_id": "BER",
    "arrival_id": "NRT",
    "outbound_date": "2026-10-09",
    "return_date": "2026-10-24",
    "travel_class": "ECONOMY",
    "adults": "2",
    "currency": "PLN",
    "country_code": "PL",
    "language_code": "pl-PL",
    "search_type": "cheap"
}

headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "google-flights2.p.rapidapi.com"
}

response = requests.get(
    url,
    headers=headers,
    params=querystring,
    timeout=60
)

data = response.json()

flights = data["data"]["itineraries"]["topFlights"]

if not flights:
    message = "❌ Nie znaleziono lotów."
else:
    cheapest = min(flights, key=lambda x: x["price"])

    message = f"""
🇯🇵 TEST LOTÓW

BER → NRT

Cena: {cheapest['price']} PLN
Czas podróży: {cheapest['duration']['text']}
Wylot: {cheapest['departure_time']}
Przylot: {cheapest['arrival_time']}
"""

webhook = os.environ["DISCORD_WEBHOOK_URL"]

requests.post(
    webhook,
    json={"content": message},
    timeout=30
)

print(message)
