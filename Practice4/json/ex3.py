import json
data = {"city": "Astana", "year": 2026}
with open("data.json", "w") as f:
    json.dump(data, f)