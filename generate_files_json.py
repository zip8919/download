import os
import json

files_directory = 'files'
files_list = []

for file_name in os.listdir(files_directory):
    file_path = os.path.join(files_directory, file_name)
    file_stats = os.stat(file_path)
    is_directory = os.path.isdir(file_path)
    size = 'Folder' if is_directory else f"{file_stats.st_size / 1024:.2f} KB"
    download_url = f"/{file_name}"

    file_info = {
        'name': file_name,
        'size': size,
        'downloadUrl': download_url,
        'isDirectory': is_directory
    }
    files_list.append(file_info)

with open('files.json', 'w') as json_file:
    json.dump({'files': files_list}, json_file, indent=2)