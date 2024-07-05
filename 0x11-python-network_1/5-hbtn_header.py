#!/usr/bin/python3
""" Fetching a url  """
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    usr_id = response.headers.get('X-Request-Id')
    print(usr_id)
