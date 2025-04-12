import requests
import urllib.parse
from config2 import apikeys as cfg


targeturl = 'https://example.com'
apikey = cfg["htmltopdfkey"]  # API key for authentication

apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'html': targeturl, 'apikey': apikey}  # parameters to be sent in the request
parsedparams = urllib.parse.urlencode(params) #parse the parameters into a query string format

print("using API key: ", apikey)

requestUrl = apiurl +"?" + parsedparams 
print (requestUrl)

response = requests.get(requestUrl)

print (response.status_code)
result =response.content

with open("document.pdf", "wb") as handler:
    handler.write(result)