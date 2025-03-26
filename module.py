import requests

ns_url = "https://example.nightscout.url/pebble" # dont forget to add /pebble to the end of your nightscout url
fetch = requests.get(ns_url)
data = fetch.json()

arrows = {
    "DoubleUp": "⬆️⬆️",
    "SingleUp": "⬆️",
    "FortyFiveUp": "↗️",
    "Flat": "➡️",
    "FortyFiveDown": "↘️",
    "SingleDown": "⬇️",
    "DoubleDown": "⬇️⬇️",
}

if "bgs" in data and len(data["bgs"]) > 0:
    bg_data = data["bgs"][0]
    sgv = bg_data.get("sgv")
    iob = bg_data.get("iob")
    cob = bg_data.get("cob")
    battery = bg_data.get("battery")
    bgdelta = bg_data.get("bgdelta")
    direction = bg_data.get("direction")
    unicodearrows = arrows.get(direction, "❓")
    #example: print(f"{sgv} {unicodearrows} IOB: {iob} COB: {cob}")
else:
    print("check if nightscout is up")
