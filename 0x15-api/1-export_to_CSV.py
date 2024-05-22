#!/usr/bin/python3
"""
    this is a python script that, makes requests to a REST API
    - accepts an integer as a parameter, which is the employee ID
"""
import requests
from sys import argv
import csv

if __name__ == "__main__":
    if len(argv) < 2 or not argv[1].isdigit():
        print("exiting...")
        exit(1)

    # obtain the employee using id passed
    id = int(argv[1])
    r_users = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')

    # obtain todo list
    r_todos = requests.get(f'https://jsonplaceholder.typicode.com/todos')

    data = []
    data_row = []
    name = r_users.json()['username']
    done_tasks_titles = []
    for item in r_todos.json():
        if item["userId"] == id:
            data_row.append(item["userId"])
            data_row.append(name)
            data_row.append(item["completed"])
            data_row.append(item["title"])
            data.append(data_row)
            data_row = []

    with open("USER_ID.csv", mode='w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
