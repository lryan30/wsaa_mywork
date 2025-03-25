import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
#print(response.json())
data = response.json()
with open ("bitcoindump.json", "w") as fp:
    json.dump(data, fp)

#euroPriceObject = data["bpi"]["EUR"]
#rate = euroPriceObject["rate"]
#print(rate)


# requests.get means that we are sending a GET request to the server.
# The server will respond with a response object. This object is stored in the variable response.
# response.json() will return the JSON object of the result.
# The JSON object is stored in the variable data.
# The data is written to a file named bitcoindump.json.
# The data is read from the file and stored in the variable euroPriceObject.    
# bitcoin dump is a file that contains the data from the server.
# dump is a method that writes the data to a file. 
# api.coindesk.com is a website that provides the current price of bitcoin.
# read in url and copy format to file.

# bpi is a dictionary that contains the price of bitcoin in different currencies.


# assignment:
# API shuffledeckcards. pass in url and it shuffles to give a deck id
# read deck id and pass in url to get cards (5)
# print the cards
# last few marks: check if the user has drawn a royal flush etc


