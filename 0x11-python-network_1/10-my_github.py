#!/usr/bin/python3
"""
    Write a Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API to display your id
"""


if __name__ == "__main__":
    from requests.auth import HTTPBasicAuth
    import requests
    from sys import argv
    auth = HTTPBasicAuth(argv[1], argv[2])
    res = requests.get('https://api.github.com/user', auth=auth)
    print(res.json().get('id'))
