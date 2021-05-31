import requests

url2021 = 'https://data.opentrack.run/en-gb/x/2021/GBR/weekly30/event/R{:02}/1/1/json/'
url2020 = 'https://data.opentrack.run/en-gb/x/2020/GBR/weekly30/event/R{:02}/1/1/json'

for i in range(1, 23):
    resp = requests.get(url2021.format(i))
    with open("output/rawfiles/ea-2021-{:02}.json".format(i), "w") as my_file:
        print("Reading week ", i)
        my_file.write(resp.text)

for i in range(1, 27):
    resp = requests.get(url2020.format(i))
    with open("output/rawfiles/ea-2020-{:02}.json".format(i), "w") as my_file:
        print("Reading week ", i)
        my_file.write(resp.text)
