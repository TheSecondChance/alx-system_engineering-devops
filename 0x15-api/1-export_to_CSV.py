#!/usr/bin/python3
"""Python script to export data in the CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    userID = sys.argv[1]
    feachUrl = "https://jsonplaceholder.typicode.com/"
    userJson = requests.get(feachUrl + "users/{}".format(userID)).json()
    userName = userJson.get("username")
    todos = requests.get(feachUrl + "todos", params={"userId": userID}).json()

    with open("{}.csv".format(userID), "w", newline="") as csvFile:
        writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [userID, userName, todo.get("completed"), todo.get("title")]
         ) for todo in todos]
