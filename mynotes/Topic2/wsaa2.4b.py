import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
