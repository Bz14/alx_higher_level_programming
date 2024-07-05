#!/usr/bin/python3
""" Fetching a url  """
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            result = response.read()
            print(result)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
