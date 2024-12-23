import os

current_work_directory = os.getcwd()
print(current_work_directory)

list_files_current_dir = os.listdir()
print(list_files_current_dir)

os.rename('./28-os.py', 'os.py')