#!/usr/bin/python3
"""Uses GitHub API to display user ID using Basic Authentication."""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    r = requests.get(url, auth=(username, token))
    print(r.json().get("id"))
