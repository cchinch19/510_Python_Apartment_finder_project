import requests
import json
import os
os.makedirs("data/processed", exist_ok=True)

API_KEY_Walkscore = 'be15a1f38e712e2712ce9d3b0092f68f'
API_KEY = 'eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjNjOGRmYzA0MTIxZTQ2OThiNDkwOWVmYjhhZDczMmQzIiwiaCI6Im11cm11cjY0In0='
url_ors = "https://api.openrouteservice.org/v2/directions/driving-car"

city_coor = {
    "Downtown Long Beach": (-118.192999, 33.772904),
    "Cerritos": (-118.055856, 33.871295),
    "Redondo Beach": (-118.385753, 33.847037),
    "Corona": (-117.57259368896486, 33.86289673758),
    "Malibu": (-118.81020784378053, 34.0198701182436)
}

usc_lon, usc_lat = -118.2851, 34.0224
work_lon, work_lat = -118.415279, 33.931539

def get_scores(lon, lat):
    url = f"https://api.walkscore.com/score?format=json&lat={lat}&lon={lon}&transit=1&bike=1&wsapikey={API_KEY_Walkscore}"
    data = requests.get(url).json()
    return {
        "walk_score": data.get("walkscore"),
        "bike_score": data.get("bike", {}).get("score"),
    }

def get_commute_time(start_lon, start_lat, end_lon, end_lat):
    headers = {"Authorization": API_KEY, "Content-Type": "application/json"}
    body = {"coordinates": [[start_lon, start_lat], [end_lon, end_lat]]}
    data = requests.post(url_ors, headers=headers, json=body).json()
    return data["routes"][0]["summary"]["duration"] // 60

def get_all_commutes(end_lon, end_lat):
    return {city: get_commute_time(coor[0], coor[1], end_lon, end_lat)
            for city, coor in city_coor.items()}

score_data = {city: get_scores(coor[0], coor[1]) for city, coor in city_coor.items()}
usc_commutes = get_all_commutes(usc_lon, usc_lat)
work_commutes = get_all_commutes(work_lon, work_lat)

with open("data/processed/scores.json", "w") as f:
    json.dump(score_data, f)
with open("data/processed/commutes.json", "w") as f:
    json.dump({"usc": usc_commutes, "work": work_commutes}, f)
print("Saved scores and commutes")
