# Open single JSON file filter unnecessary keys and add id
import json

with open('paste the file path', 'r') as openfile:
    json_object = json.load(openfile)

# feet = (json_object['properties']["feet"])
# meters = (json_object['properties']["meters"])
# latitude = (json_object['properties']["latitude"])
# longitude = (json_object['properties']["longitude"])
# name = (json_object['properties']["name"])
# regions = (json_object['properties']["regions"])
# countries = (json_object['properties']["countries"])
#
# dictionary_peak = {
#     "feet": feet,
#     "meters": meters,
#     "latitude": latitude,
#     "longitude": longitude,
#     "name": name,
#     "region": regions,
#     "country": countries,
# }

counter = 0

for i in json_object["features"]:

    counter = counter + 1

    i["properties"]["id"] = counter
    del i["properties"]["marker-size"]
    del i["properties"]["marker-symbol"]
    json_data = json.dumps(i["properties"], indent=4)

    with open("peaks_data", "a") as outfile:
        outfile.write(json_data)