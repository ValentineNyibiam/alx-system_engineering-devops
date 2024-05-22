#!/usr/bin/python3
"""
    this is a python script that, makes requests to a REST API
    - exports the data in the json format for all employees
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    # obtain the employees
    r_users = requests.get(users_url).json()

    # obtain todo list
    r_todos = requests.get(todos_url).json()

    main_dict = {}
    list_item = {}
    dict_value = []
    id = 0
    index = 1
    total_ids = len(r_users)
    while (index <= total_ids):
        name = r_users[id]["username"]
        for item in r_todos:
            if item["userId"] == index:
                list_item.update({"username": name})
                list_item.update({"task": item["title"]})
                list_item.update({"completed": item["completed"]})
                dict_value.append(list_item)
                list_item = {}
        main_dict.update({index: dict_value})
        index += 1
        id += 1

    with open(f"todo_all_employees.json", mode='w') as file:
        json.dump(main_dict, file)
