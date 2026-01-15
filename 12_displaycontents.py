import os

def display_directory(path, level=0):
    items = os.listdir(path)

    for item in items:
        item_path = os.path.join(path, item)
        print("  " * level, end="")

        if os.path.isdir(item_path):
            print(f"Folder: {item}")
            display_directory(item_path, level + 1)
        else:
            file_name, file_type = os.path.splitext(item)
            print(f"File: {file_name} | Type: {file_type}")


folder_path = "C:/Users/Student/Documents"
display_directory(folder_path)
