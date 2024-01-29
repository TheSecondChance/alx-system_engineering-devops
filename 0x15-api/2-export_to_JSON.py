#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    feachUrl = "https://jsonplaceholder.typicode.com/"
    userJson = requests.get(feachUrl + "users/{}".format(userId)).json()
    userName = userJson.get("username")
    todos = requests.get(feachUrl + "todos", params={"userId": userId}).json()

    with open("{}.json".format(userId), "w") as jsonFile:
        json.dump({userId: [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": userName
            } for todo in todos]}, jsonFile)
