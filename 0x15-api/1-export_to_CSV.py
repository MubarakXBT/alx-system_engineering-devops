#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the CSV format.
"""
import csv
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

    data = []
    for task in file:
        if task["completed"] is True:
            dic = {'USER_ID': ID, 'USERNAME': username,
                   'TASK_COMPLETED_STATUS': True, 'TASK_TITLE': task["title"]}
            data.append(dic)
        else:
            dic = {'USER_ID': ID, 'USERNAME': username,
                   'TASK_COMPLETED_STATUS': False, 'TASK_TITLE': task["title"]}
            data.append(dic)

    fields = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    with open("{}.csv".format(ID), mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields, quoting=csv.QUOTE_ALL)

        for row in data:
            writer.writerow(row)
