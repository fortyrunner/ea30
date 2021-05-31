import json
import csv

with open('output/results-2021.csv', 'w', newline='') as output_file:
    csv_file = csv.writer(output_file)
    csv_file.writerow(["Week", "Date", "Name", "Place", "Category", "Category Position", "Distance"])
    for i in range(1, 23):
        with open('output/rawfiles/ea{:02}.json'.format(i), "r") as my_file:
            contents = my_file.read()
            parsed = json.loads(contents)
            eventName = parsed["event_name"]
            results = parsed["results"]
            for result in results:
                if result["team"] == "ARE80":
                    distance = result["athlon_points"]
                    csv_file.writerow([i, eventName, result["first_name"] + " " + result["last_name"], result["place"],
                                       result["category"], result["catpos"], distance])
