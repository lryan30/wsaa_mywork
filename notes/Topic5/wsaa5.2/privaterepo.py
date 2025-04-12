

import requests
import json
#from config import config as cfg

filename = "repos-private.json"

url = "https://api.github.com/repos/andrewbeattycourseware/wsaa-course-material/contents/aprivateone"

apikey = "github_pat_xxxxxxxxxxxxxxxB5TX5GGQhxxxxxxxxxxxx"

response = requests.get(url, auth=('token', apikey))
print(response.status_code)

with open(filename, 'w') as fp:
    repojson = response.json()
    json.dump(response.json(), fp, indent=4)

