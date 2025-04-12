

# This code retrieves public repositories for a specified GitHub user,
# and saves the information in a JSON file.

import requests
import json

filename = "wsaa-public.json"

#url = 'https://api.github.com/users/lryan30/repos?per_page=100'    
contents_url = "https://api.github.com/repos/andrewbeattycourseware/wsaa-course-material/contents/code"


repsonse = requests.get(contents_url)
print(repsonse.status_code)

repoJson = repsonse.json()
# print(repoJson)

with open(filename, 'w') as fp:
    json.dump(repoJson, fp, indent=4)




# contents"_url": "https://api.github.com/repos/lcontentsryan30/wsaa_mywork/contents/{+path}


# if want to look at contents of certain folders in the repo, use this url:
# https://api.github.com/repos/lcontentsryan30/wsaa_mywork/contents/labs/Topic5/wsaa5.1/apikey.py