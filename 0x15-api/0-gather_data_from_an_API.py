#!/usr/bin/python3
"""
    this is a python script that, makes requests to a REST API
    - accepts an integer as a parameter, which is the employee ID
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2 or not argv[1].isdigit():
        print("exiting...")
        exit(1)

    # obtain the employee using id passed
    id = int(argv[1])
    r_users = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')

    # obtain todo list
    r_todos = requests.get(f'https://jsonplaceholder.typicode.com/todos')

    done_tasks = 0
    tasks = 0
    done_tasks_titles = []
    for item in r_todos.json():
        if item["userId"] == id:
            if item["completed"]:
                done_tasks_titles.append(item["title"])
                done_tasks += 1
                tasks += 1
            else:
                tasks += 1

    employee_name = r_users.json()['name']
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{tasks}):")

    for item in done_tasks_titles:
        print(f"\t{item}", end='\n')
