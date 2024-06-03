#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    ID = sys.argv[1]
    API = "https://jsonplaceholder.typicode.com/users/{}".format(ID)

    response = requests.get(API)
    username = response.json().get("username")

    todo_api = API + "/todos"
    response = requests.get(todo_api)
    file = response.json()

    data = {ID: []}
    for task in file:
        dictionary[ID].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(ID), 'w') as filename:
        json.dump(data, filename)
