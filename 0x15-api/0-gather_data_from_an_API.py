#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.

Requirements:
    You must use urllib or requests module
    The script must accept an integer as a parameter, which is the employee ID
    The script must display on the standard output the employee TODO list progress in this exact format:

    First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
import sys
import requests


if __name__ == "__main__":
    ID = sys.argv[1]
    API = "https://jsonplaceholder.typicode.com/users/{}".format(ID)

    response = requests.get(API)
    name = response.json().get("name")

    todo_api = API + "/todos"
    response = requests.get(todo_api)
    file = response.json()

    total_task = 0
    done = 0
    task_title = []
    for task in file:
        total_task += 1
        if task["completed"] is True:
            task_title.append(task["title"])
            done += 1
    print("Employee {} is done with tasks({}/{}):".format(name, done, total_task))
    for task in task_title:
        print("\t", task)
