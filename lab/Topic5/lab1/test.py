import requests
import json
import lab.Topic5.lab2.config as cfg


repo_url = 'https://api.github.com/repos/lryan30/aprivateone'  
branches_url = f'{repo_url}/branches'
commits_url = f'{repo_url}/commits'
pulls_url = f'{repo_url}/pulls'
issues_url = f'{repo_url}/issues'


apiKey = cfg.githubkey


repo_response = requests.get(repo_url, auth=('token', apiKey))
repo_info = repo_response.json()


branches_response = requests.get(branches_url, auth=('token', apiKey))
branches_info = branches_response.json()


commits_response = requests.get(commits_url, auth=('token', apiKey))
commits_info = commits_response.json()


pulls_response = requests.get(pulls_url, auth=('token', apiKey))
pulls_info = pulls_response.json()


issues_response = requests.get(issues_url, auth=('token', apiKey))
issues_info = issues_response.json()




repo_data = {
    "repository_info": repo_info,
    "branches": branches_info,
    "commits": commits_info,
    "pull_requests": pulls_info,
    "issues": issues_info    
}

with open("repository_details.json", 'w') as fp:
    json.dump(repo_data, fp, indent=4)

print("Repo details saved.json")
