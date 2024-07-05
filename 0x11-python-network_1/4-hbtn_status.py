#!/usr/bin/python3
""" Fetching a url  """
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
    print("\t- utf8 content: {}".format(response.text.encode('utf-8')))
