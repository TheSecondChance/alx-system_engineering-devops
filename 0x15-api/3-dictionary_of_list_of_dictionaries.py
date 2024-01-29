#!/usr/bin/python3
"""Python script to export data in the JSON format
"""
import json
import requests

if __name__ == "__main__":
    feachUrl = "https://jsonplaceholder.typicode.com/"
    usersJson = requests.get(feachUrl + "users/").json()

    with open("todo_all_employees.json", "w") as jsonFile:
        json.dump({
            userId.get("id"): [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": userId.get("username")
            } for todo in requests.get(
                feachUrl + "todos", params={"userId": userId.get(
                    "id")}).json()]
            for userId in usersJson}, jsonFile)
