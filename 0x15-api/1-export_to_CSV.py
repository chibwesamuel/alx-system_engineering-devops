#!/usr/bin/python3
import csv
import requests

def export_employee_todo_progress_to_csv(employee_id):
    """
    Exports an employee's TODO list progress to a CSV file in the specified format.

    Args:
        employee_id (int): The ID of the employee to export progress for.

    Returns:
        None.
    """
    # Make the API request
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    # Parse the response
    tasks = response.json()
    employee_name = tasks[0]['username']
    filename = f"{employee_id}.csv"

    # Write the CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            writer.writerow([task['userId'], employee_name, task['completed'], task['title']])

# Example usage
export_employee_todo_progress_to_csv(1)
