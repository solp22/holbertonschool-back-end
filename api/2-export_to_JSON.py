#!/usr/bin/python3
"""exporting data to csv"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    to_do = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}")
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    username = user.json().get('username')

    with open(f"{argv[1]}.json", 'w', encoding="utf-8") as f:
        task_list = []
        user_dict = {}
        user_dict[f"{argv[1]}"] = task_list

        for task in to_do.json():
            comp = task.get('completed')
            tit = task.get('title')
            task_list.append(dict(task=tit, completed=comp, username=username))

        json.dump(user_dict, f)
