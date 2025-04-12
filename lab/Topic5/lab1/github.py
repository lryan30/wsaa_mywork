import requests
import json
import lab.Topic5.lab2.config as cfg

url = 'https://api.github.com/repos/lryan30/aprivateone'

apiKey = cfg.githubkey

response = requests.get(url, auth=('token', apiKey))
print(response.status_code)

repoJSON = response.json()

# Save the repository details in a JSON file
with open("aprivateone.json", 'w') as fp:
    json.dump(repoJSON, fp, indent=4)

