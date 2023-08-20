# Open multiple JSON files. Filter unnecessary data and add id
import json
import os

base_dir = 'paste the folder path separate by \\'
output = []

for file in os.listdir(base_dir):

    # if '_index.geojson' not in file:
    with open(f'{base_dir}\\{file}', 'r') as open_file:
        json_object = json.load(open_file)

        json_file = json.dumps(json_object, indent=4)

        for i in json_object["features"]:
            if i["properties"]["feet"] >= 6561.68:
                del i["properties"]["marker-size"]
                del i["properties"]["marker-symbol"]
                output.append(i["properties"])

counter = 0
for i in output:
    counter = counter + 1
    i["id"] = counter

json_data = json.dumps(output, indent=6, separators=(",", ":"))
with open("all_peaks_over_2000_meters_data", "a") as outfile:
    outfile.write(json_data)