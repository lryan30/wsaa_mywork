import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
#print(response.json())
data = response.json()
with open ("bitcoindump.json", "w") as fp:
    json.dump(data, fp)

euroPriceObject = data["bpi"]["EUR"]
rate = euroPriceObject["rate"]
print(rate)

# This code reads the JSON file from the cloud and prints the rate of Bitcoin in Euros.
