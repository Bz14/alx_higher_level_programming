#!/usr/bin/python3
""" Fetching a url  """
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    data = {"q": q}
    response = requests.post(url, data=data)
    if (response.headers.get('content-type')
        == 'application/json'):
        response_data = response.json()
        if response_json:
            print(("[{}] {}"
                   .format(response_json['id'], response_json['name'])))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
