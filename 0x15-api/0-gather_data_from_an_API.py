#!/usr/bin/python3
"""python script that uses API to get info about employee """
import requests
import sys


if __name__ == "__main__":
    feachUrl = "https://jsonplaceholder.typicode.com/"
    employeeId = sys.argv[1]
    userRsponse = requests.get(feachUrl + "users/{}".format(
        employeeId))
    userResponsJason = userRsponse.json()
    params = {"userId": employeeId}
    todosRespons = requests.get(feachUrl + "todos",
                                params=params)
    todos = todosRespons.json()
    taskCompleted = []
    for todo in todos:
        if todo.get("completed") is True:
            taskCompleted.append(todo.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(userResponsJason.get(
        "name"), len(taskCompleted), len(todos)))

    for Completed in taskCompleted:
        print("\t {}".format(Completed))
