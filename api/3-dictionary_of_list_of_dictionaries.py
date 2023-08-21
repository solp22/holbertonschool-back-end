#!/usr/bin/python3
"""exporting data to csv"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    to_do = requests.get(
        f"https://jsonplaceholder.typicode.com/todos")
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/")

    with open("todo_all_employees.json", 'w', encoding="utf-8") as f:
        user_dict = {}

        for employee in user.json():
            task_list = []
            username = employee.get('username')
            for task in to_do.json():
                if employee.get('id') == task.get('userId'):
                    comp = task.get('completed')
                    tit = task.get('title')
                    task_list.append(
                        dict(task=tit, completed=comp, username=username))
            user_dict[employee.get('id')] = task_list

        json.dump(user_dict, f)
