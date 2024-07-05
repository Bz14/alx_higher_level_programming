#!/usr/bin/python3
""" Fetching a url  """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {"email": email}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        result = response.read()
        print("Your email is: {}".format(result.decode('utf-8')))
