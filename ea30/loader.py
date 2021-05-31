import requests

url = "https://data.opentrack.run/en-gb/x/2021/GBR/weekly30/event/R{:02}/1/1/json/"

for i in range(1, 22):
    resp = requests.get(url.format(i))
    with open("output/rawfiles/ea{:02}.json".format(i), "w") as my_file:
        print("Reading week ", i)
        my_file.write(resp.text)
