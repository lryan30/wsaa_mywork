import requests

url = "http://www.atu.ie"

response = requests.get(url)
print(response.status_code)

# This code sends a request to the website atu.ie and prints the status code of the response.
# 502 is server error -->bad gateway error. 