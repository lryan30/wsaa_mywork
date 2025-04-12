# This program generates a URL for an API request to convert a webpage to a PDF using the html2pdf API.


import requests
import urllib.parse
from config import apikeys as cfg


targeturl = 'https://en.wikipedia.org'


#apikey = cfg["htmltopdfkey"]  # API key for authentication
# The API key is stored in a separate configuration file (config.py) for security and convenience.

apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'url': targeturl, 'apikey': apikey}  # parameters to be sent in the request
parsedparams = urllib.parse.urlencode(params) #parse the parameters into a query string format

requesturl = apiurl + '?' + parsedparams   # '?' is used to separate the base URL from the query parameters
#print(requesturl)

requestUrl = apiurl +"?" + parsedparams 
print (requestUrl)

response = requests.get(requestUrl)

print (response.status_code)
result =response.content

with open("document.pdf", "wb") as handler:
    handler.write(result)
#print("using API key: ", apikey)





# generates a URL for an API request to convert a webpage to a PDF using the html2pdf API.
# It constructs the request URL by encoding the target URL and API key as query parameters.
# The generated URL can be used to send a request to the API for PDF conversion.
# The program uses the requests library to handle HTTP requests and the urllib.parse module to encode the parameters.

# The target URL is set to the Wikipedia homepage, and the API key is provided for authentication.
# The base API URL is defined, and the parameters are encoded into a query string format.