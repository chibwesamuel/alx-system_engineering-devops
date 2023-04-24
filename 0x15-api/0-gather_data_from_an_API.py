#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python todo.py EMPLOYEE_ID")
    sys.exit(1)

employee_id = sys.argv[1]
url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
response = requests.get(url)

if response.status_code != 200:
    print("Error retrieving data")
    sys.exit(1)

todos = response.json()

employee_name = todos[0]["name"]
total_tasks = len(todos)
done_tasks = sum(todo["completed"] for todo in todos)
done_titles = [todo["title"] for todo in todos if todo["completed"]]

print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
for title in done_titles:
    print(f"\t {title}")
