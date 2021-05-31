import json

print("week,date,first,last,cat,catpos,distance")
for i in range(1, 22):
    with open("output/rawfiles/ea{:02}.json".format(i), "r") as my_file:
        contents = my_file.read()
        parsed = json.loads(contents)
        eventName = parsed["event_name"]
        results = parsed["results"]
        for result in results:
            team = result["team"]
            if team == "ARE80":
                distance = result["athlon_points"]
                print(i, ",", eventName, ",", result["first_name"], result["last_name"], ",", result["category"], ",", result["catpos"], ",", distance)