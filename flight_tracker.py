import os
import requests

api_key = os.environ["RAPIDAPI_KEY"]

url = "https://google-flights2.p.rapidapi.com/api/v1/searchFlights"

headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "google-flights2.p.rapidapi.com"
}

searches = [
    {
        "name": "WAW-NRT",
        "departure_id": "WAW",
        "arrival_id": "NRT",
        "outbound_date": "2027-05-07",
        "return_date": "2027-05-21",
    },
    {
        "name": "BER-NRT",
        "departure_id": "BER",
        "arrival_id": "NRT",
        "outbound_date": "2027-05-07",
        "return_date": "2027-05-21",
    },
    {
        "name": "BER-HND",
        "departure_id": "BER",
        "arrival_id": "HND",
        "outbound_date": "2027-05-07",
        "return_date": "2027-05-21",
    },
]

results = []

for search in searches:

    querystring = {
        "departure_id": search["departure_id"],
        "arrival_id": search["arrival_id"],
        "outbound_date": search["outbound_date"],
        "return_date": search["return_date"],
        "travel_class": "ECONOMY",
        "adults": "2",
        "currency": "PLN",
        "country_code": "PL",
        "language_code": "en-US",
        "search_type": "cheap"
    }

    response = requests.get(
        url,
        headers=headers,
        params=querystring,
        timeout=60
    )

    data = response.json()

    try:
        flights = data["data"]["itineraries"]["topFlights"]

        if flights:
            cheapest = min(flights, key=lambda x: x["price"])
            results.append(
                f"{search['name']} -> {cheapest['price']} PLN"
            )
        else:
            results.append(
                f"{search['name']} -> BRAK LOTÓW"
            )

    except Exception:
        results.append(
            f"{search['name']} -> BŁĄD"
        )

message = "🇯🇵 TEST WIELU TRAS\n\n" + "\n".join(results)

webhook = os.environ["DISCORD_WEBHOOK_URL"]

requests.post(
    webhook,
    json={"content": message},
    timeout=30
)

print(message)
