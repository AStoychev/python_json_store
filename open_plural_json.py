# Open multiple JSON files. Filter unnecessary data and add id
import json
import os

base_dir = 'paste the folder path'

for file in os.listdir(base_dir):

    if '_index.geojson' not in file:
        with open(f'{base_dir}\\{file}', 'r') as open_file:
            json_object = json.load(open_file)

            counter = 0
            json_file = json.dumps(json_object, indent=4)

            for i in json_object["features"]:
                counter = counter + 1
                i["properties"]["id"] = counter
                del i["properties"]["marker-size"]
                del i["properties"]["marker-symbol"]
                json_data = json.dumps(i["properties"], indent=4)
                with open("all_peaks_data", "a") as outfile:
                    outfile.write(json_data)
