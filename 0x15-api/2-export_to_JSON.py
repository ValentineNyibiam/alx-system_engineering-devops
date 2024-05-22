#!/usr/bin/python3
"""
    this is a python script that, makes requests to a REST API
    - accepts an integer as a parameter, which is the employee ID
    - exports the data in the json format
"""
import json
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

    main_dict = {}
    list_item = {}
    dict_value = []
    name = r_users.json()['username']
    for item in r_todos.json():
        if item["userId"] == id:
            list_item.update({"task": item["title"]})
            list_item.update({"completed": item["completed"]})
            list_item.update({"username": name})
            dict_value.append(list_item)
            list_item = {}
    main_dict.update({id: dict_value})

    with open(f"{id}.json", mode='w') as file:
        json.dump(main_dict, file)
