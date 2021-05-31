import json
import csv

def parse(year, end):
    with open('output/results-{:04}.csv'.format(year), 'w', newline='') as output_file:
        csv_file = csv.writer(output_file)
        csv_file.writerow(["Week", "Date", "Name", "Place", "Category", "Category Position", "Distance"])
        for i in range(1, end):
            with open('output/rawfiles/ea-{:04}-{:02}.json'.format(year, i), "r") as my_file:
                contents = my_file.read()
                parsed = json.loads(contents)
                eventName = parsed["event_name"]
                results = parsed["results"]
                for result in results:
                    if result["team"] == "ARE80":
                        distance = result["athlon_points"]
                        csv_file.writerow([i, eventName, result["first_name"] + " " + result["last_name"], result["place"],
                                           result["category"], result["catpos"], distance])
parse(2021, 23)
parse(2020, 27)