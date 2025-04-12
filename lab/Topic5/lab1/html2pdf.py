
import requests
import urllib.parse
import lab.Topic5.lab2.config as cfg

targeturl = 'https://example.com'

apikey = cfg.htmltopdfkey  # API key for authentication 

apikeyurl = 'https://api.html2pdf.app/v1/generate'

# Parameters to be sent in the request 
params = {'html': targeturl, 'apiKey': apikey}  # 
parsedparams = urllib.parse.urlencode(params)  # parse the parameters into a query string format
requesturl = apikeyurl + '?' + parsedparams  # '?' separates the base URL from the query parameters

response = requests.get(requesturl)
print(response.status_code)

# Check if the request was successful
if response.status_code == 200:
    result = response.content
    with open("document.pdf", "wb") as handler:
        handler.write(result)
else:
    print("Failed to retrieve the PDF. Status code:", response.status_code)
    print(response.text)  
