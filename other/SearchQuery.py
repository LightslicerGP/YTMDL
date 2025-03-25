import requests
import json

link = "https://itunes.apple.com/search?term=MINION%20(with%20salem%20ilese)%20CG5&entity=song"

response = requests.get(link)

with open("SearchQueryList.json", "w") as file:
    json.dump(response.json(), file, indent=2)
