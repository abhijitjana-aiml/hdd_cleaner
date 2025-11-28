import os

def get_all_files(base_path: str):
    """Return all file paths inside HDD."""
    file_list = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list
