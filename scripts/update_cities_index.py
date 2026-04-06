import json
import os

data_dir = "data/cities"
output_file = "data/cities/cities-index.json"

city_files = [f for f in os.listdir(data_dir) if f.endswith('.json') and f != 'cities-index.json']
cities_index = []

for file in city_files:
    with open(os.path.join(data_dir, file), 'r') as f:
        data = json.load(f)
        cities_index.append({
            "city": data["city"],
            "state": data["state"],
            "slug": data["slug"],
            "stateAbbr": data["state"]
        })

with open(output_file, 'w') as f:
    json.dump(cities_index, f, indent=2)

print(f"Generated cities-index.json with {len(cities_index)} cities")
