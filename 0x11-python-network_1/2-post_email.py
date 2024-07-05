#!/usr/bin/python3
""" Fetching a url  """
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {"email": email}
    data = urllib.parse.urlencode(values)
    full_url = url + "?" + data
    with urllib.request.urlopen(full_url) as response:
        result = response.read()
        print("Your email is: {}".format(result.decode('utf-8')))
