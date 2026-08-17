#!/usr/bin/python3
"""Sends a POST request to search a user with a letter parameter."""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': q}

    try:
        r = requests.post(url, data=payload)
        json_data = r.json()
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
