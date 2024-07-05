#!/usr/bin/python3
""" Fetching a url  """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    usr_id = response.headers.get('X-Request-Id')
    print(usr_id)
