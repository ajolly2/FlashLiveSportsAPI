import os
import requests
from retry import retry
from datetime import datetime
import json

RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")
if not RAPIDAPI_KEY:
    raise Exception("RAPIDAPI_KEY environment variable not set.")

@retry(Exception, tries=3, delay=2)
def fetch_flashlive_events():
    url = "https://flashlive-sports.p.rapidapi.com/v1/events/list"
    params = {
        "sport_id": "1",  # 1 = Soccer. See docs for other sports
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "locale": "en_INT",
        "page": "1"
    }
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "flashlive-sports.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    events = fetch_flashlive_events()
    with open("live_games.json", "w") as f:
        json.dump(events, f, indent=2)
    print("Fetched and saved live games to live_games.json")
