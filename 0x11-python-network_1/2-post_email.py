#!/usr/bin/python3
""" Fetching a url  """
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {"email": email}
    data = urllib.parse.urlencode(values).encode('utf-8')
    res = urllib.request.Request(url, data)
    with urllib.request.urlopen(res) as response:
        result = response.read()
        print("Your email is: {}".format(result.decode('utf-8')))
