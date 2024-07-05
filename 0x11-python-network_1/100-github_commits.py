#!/usr/bin/python3
""" Fetching a url  """
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = ("https://api.github.com/repos/{}/{}/commits"
           .format(owner, repo))
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[0:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print("{}: {}".format(sha, author_name))
