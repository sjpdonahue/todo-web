def get_todos(filepath='todos.txt'):
    """Open file and return contents as a list."""
    with open(filepath) as file_read:
        gotten_todos = file_read.readlines()
    return gotten_todos


def write(todos_local, filepath='todos.txt'):
    """Write todos list to the specified file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_local)


def show(todos_local):
    """Print the todos list in a user-friendly format."""
    for index, item in enumerate(todos_local):
        item = item.strip('\n')
        print(f"{index + 1}. {item}")

