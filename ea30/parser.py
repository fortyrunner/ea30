import json
import csv

def parse(year, end, totals_file):
    with open('output/results-{:04}.csv'.format(year), 'w', newline='') as output_file:
        csv_file = csv.writer(output_file)
        csv_file.writerow(["Year", "Week", "Date", "Name", "Place", "Category", "Category Position", "Distance"])
        for i in range(1, end):
            with open('output/rawfiles/ea-{:04}-{:02}.json'.format(year, i), "r") as my_file:
                contents = my_file.read()
                parsed = json.loads(contents)
                eventName = parsed["event_name"]
                results = parsed["results"]
                for result in results:
                    if result["team"] == "ARE80":
                        distance = result["athlon_points"]
                        csv_file.writerow([year, i, eventName, result["first_name"] + " " + result["last_name"], result["place"],
                                           result["category"], result["catpos"], distance])
                        totals_file.writerow([year, i, eventName, result["first_name"] + " " + result["last_name"], result["place"],
                                           result["category"], result["catpos"], distance])

with open('output/combined-results.csv', 'w', newline='') as results_file:
    totals_file = csv.writer(results_file)
    totals_file.writerow(["Year", "Week", "Date", "Name", "Place", "Category", "Category Position", "Distance"])
    parse(2020, 27, totals_file)
    parse(2021, 23, totals_file)
