#!/usr/bin/python3
"""exporting data to csv"""
import requests
from sys import argv

if __name__ == "__main__":
    to_do = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}")
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    username = user.json().get('username')

    with open(f"{argv[1]}.csv", 'w', encoding="utf-8") as f:
        for task in to_do.json():
            comp = task.get('completed')
            tit = task.get('title')
            f.write(
                f'"{argv[1]}","{username}","{comp}","{tit}" \n')
