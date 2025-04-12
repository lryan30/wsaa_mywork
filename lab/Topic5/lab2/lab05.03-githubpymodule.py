# PyGithub is a Python library that provides a simpler way to interact with the GitHub API.
# easier than making HTTP requests directly.

# test that the PyGithub module is installed and working

from github import Github
import config as cfg  # This assumes config.py is in the same folder
import requests
import urllib.parse

apiKey = cfg.githubkey  # Access the token from config.py

g = Github(apiKey)

#for repo in g.get_user().get_repos():
   # print(repo.name)


# modify the program to get the clone of the URL of the repo.
# put a file called test.txt in the repo and push it to the repo.

g = Github(apiKey)
repo = g.get_repo("lryan30/wsaa_mywork")
print(repo.clone_url)  # Print the clone URL of the repository

# add file test.txt to the repo

fileinfo = repo.get_contents("test.txt")
urlforfile = fileinfo.download_url
print(urlforfile)  # Print the URL of the file in the repository

