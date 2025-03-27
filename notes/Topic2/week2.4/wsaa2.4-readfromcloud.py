import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
#print (response.json())
data = response.json()
#with open ("bitcoindump.json", "w") as fp:
#    json.dump(data, fp)

# after the above line is commented out, the code will not write the data to a file
# and the data will be stored in the variable data

bpi = data["bpi"]
#print(bpi)
rate = bpi["USD"]["rate"]
print(rate)


# This code reads the JSON file from the cloud and prints the rate of Bitcoin in US