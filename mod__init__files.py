# A python script to find any empty instances of __init__ in a django project
# and insert a comment, making sure they upload to dropbox properly for proj
# submission.

import os

def is_blank(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        return not content.strip()  # Check if content is blank

def replace_init_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file == "__init__.py":
                file_path = os.path.join(root, file)
                if is_blank(file_path):
                    print(f"Found blank file: {file_path}")
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write("# initialisation code goes here "
                                "(DropBox won't allow empty uploads)")

# Get the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))
replace_init_files(script_dir)