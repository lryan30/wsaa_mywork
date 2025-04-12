import requests
import urllib.parse
import lab.Topic5.lab2.config as cfg

targeturl = 'https://en.wikipedia.org/wiki/Python_(programming_language)'  


apikey = cfg.htmltopdfkey

apikeyurl = 'https://api.html2pdf.app/v1/generate'

# Parameters for the API request
params = {'html': targeturl, 'apiKey': apikey}  # Correct API parameters
parsedparams = urllib.parse.urlencode(params)  # URL-encode the parameters
requesturl = apikeyurl + '?' + parsedparams  # Build the full request URL
response = requests.get(requesturl)


if response.status_code == 200:
    # Save the PDF content to a file
    with open("wikipedia_page_python.pdf", "wb") as f:
        f.write(response.content)
    print("Successfully saved PDF: wikipedia_page_python.pdf")
else:
    print(f"Failed to retrieve PDF. Status code: {response.status_code}")
    print(response.text)
