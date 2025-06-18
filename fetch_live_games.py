import requests
import os
import json

# --- CONFIG ---
RAPIDAPI_KEY = os.environ["RAPIDAPI_KEY"]
URL = "https://flashlive-sports.p.rapidapi.com/v1/events/list"
PARAMS = {
    "locale": "en_INT",
    "timezone": "-4",           # adjust if needed
    "sport_id": "1",            # soccer
    "indent_days": "0",         # today
}
HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "flashlive-sports.p.rapidapi.com"
}

def fetch_events():
    resp = requests.get(URL, params=PARAMS, headers=HEADERS)
    resp.raise_for_status()
    return resp.json()

def parse_events(raw):
    # List of parsed games (you can add more fields if you want!)
    games = []
    events = raw.get("DATA", [])
    for ev in events:
        games.append({
            "event_id": ev.get("EVENT_ID"),
            "start_time": ev.get("START_TIME"),
            "stage": ev.get("STAGE"),
            "round": ev.get("ROUND"),
            "home": {
                "name": ev.get("HOME_NAME"),
                "short": ev.get("SHORTNAME_HOME"),
                "logo": ev.get("IMP"),  # image path, may need to build full URL
                "participant_id": ev.get("HOME_EVENT_PARTICIPANT_ID"),
                "goals": ev.get("HOME_GOAL_VAR"),
            },
            "away": {
                "name": ev.get("AWAY_NAME"),
                "short": ev.get("SHORTNAME_AWAY"),
                "logo": ev.get("IMP"),  # image path, may need to build full URL
                "participant_id": ev.get("AWAY_EVENT_PARTICIPANT_ID"),
                "goals": ev.get("AWAY_GOAL_VAR"),
            },
        })
    return games

if __name__ == "__main__":
    raw = fetch_events()
    games = parse_events(raw)
    with open("live_games.json", "w") as f:
        json.dump(games, f, indent=2)
    print(f"Fetched {len(games)} live games.")
