#!/usr/bin/python3
"""exporting data to csv"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    usr_id = 1
    to_do = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={usr_id}")
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/")

    with open("todo_all_employees.json", 'w', encoding="utf-8") as f:
        task_list = []
        user_dict = {}

        for employee in user.json():
            username = employee.get('username')
            for task in to_do.json():
                comp = task.get('completed')
                tit = task.get('title')
                task_list.append(dict(task=tit, completed=comp, username=username))
            user_dict[usr_id] = task_list
            usr_id = usr_id + 1

        json.dump(user_dict, f)
