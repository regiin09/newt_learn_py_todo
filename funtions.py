def load_todos(file_name='todo.txt'):
    """Load todos from the file. If the file does not exist, return an empty list."""
    try:
        with open(file_name, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist


def save_todos(todos, file_name='todo.txt'):
    """Save todos to the file by writing all todos to it."""
    with open(file_name, 'w') as file:
        file.writelines(todos)


def add_todo(todo_text, todo_list, file_name='todo.txt'):
    """Add a new todo to the list and append it to the file."""
    todo_list.append(todo_text + "\n")  # Append new todo to the list
    with open(file_name, 'a') as file:  # Open file in append mode
        file.write(todo_text + "\n")


def show_todos(todo_list):
    """Display all todos in a numbered list format."""
    if not todo_list:
        print("No todos available!")
    else:
        for index, todo_text in enumerate(todo_list):
            print(f"{index} - {todo_text.strip()}")  # Display todos with their index


def edit_todo(index, todo_list, file_name='todo.txt'):
    """Edit a todo item at a given index."""
    if 0 <= index < len(todo_list):  # Check if index is valid
        print(f"{todo_list[index].strip()} - is the current todo")
        todo_list[index] = input("Enter updated todo: ") + "\n"  # Update todo
        save_todos(todo_list, file_name)  # Save changes to the file
    else:
        print("Invalid todo number!")


def complete_todo(index, todo_list, file_name='todo.txt'):
    """Mark a todo as completed by removing it from the list."""
    if 0 <= index < len(todo_list):  # Validate index
        todo_list.pop(index)  # Remove the completed todo
        save_todos(todo_list, file_name)  # Save updated list to file
    else:
        print("Invalid todo number!")