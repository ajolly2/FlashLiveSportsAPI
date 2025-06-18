import requests
import datetime

RAPIDAPI_KEY = "69ddc401b2msh5094062915b5fe7p10d075jsne1f319ac3519"
TOURNAMENT_ID = "0bQaeJD7"  # FIFA Club World Cup

today = datetime.datetime.utcnow().strftime("%Y-%m-%d")

url = "https://flashlive-sports.p.rapidapi.com/v1/events/list"
params = {
    "sport_id": "1",
    "tournament_id": TOURNAMENT_ID,
    "date": today,
    "locale": "en_INT",
    "page": "1"
}
headers = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "flashlive-sports.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
