import requests
import json
from datetime import datetime

# FlashLive tournament_id for FIFA Club World Cup
TOURNAMENT_ID = "YoSkIXsp"  # <-- replace if you want a different league

today = datetime.utcnow().strftime('%Y-%m-%d')

url = "https://flashlive-sports.p.rapidapi.com/v1/events/list"
headers = {
    "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
    "X-RapidAPI-Host": "flashlive-sports.p.rapidapi.com"
}
params = {
    "sport_id": "1",              # Soccer
    "tournament_id": TOURNAMENT_ID,
    "date": today,
    "locale": "en_INT",
    "page": 1
}

resp = requests.get(url, headers=headers, params=params)
if resp.ok:
    data = resp.json()
else:
    print("API ERROR", resp.status_code, resp.text)
    data = {}

with open("live_games.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
