#!/usr/bin/python3
"""gathering data :)"""
import requests
from sys import argv


if __name__ == "__main__":
    to_do = requests.get(
        f"https://jsonplaceholder.typicode.com/todos/todos?userId={argv[1]}")
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/todos/users/{argv[1]}")
    employee_name = user.get('name')
    done_tasks = 0
    total_tasks = 0
    task_titles = []

    for task in to_do:
        if to_do.get('comlpeted') == 'True':
            done_tasks = done_tasks + 1
            total_tasks = total_tasks + 1
            task_titles.append(task.get('title'))
        else:
            total_tasks = total_tasks + 1

    print(f"Employee {employee_name} is done with", end="")
    print(f"tasks({done_tasks}/{total_tasks}):")
    for task in task_titles:
        print(f"/t  {task}")
