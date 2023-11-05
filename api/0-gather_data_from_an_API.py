import requests

def todo_list_progress(employee_id):
    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch todo data
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = len([task for task in todos_data if task['completed']])
    task_titles = [task['title'] for task in todos_data if task['completed']]

    # Print progress
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for title in task_titles:
        print("\t " + title)

# Test the function with an example employee_id
todo_list_progress(1)

