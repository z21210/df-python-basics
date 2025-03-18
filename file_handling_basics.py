# # Import the os module to work with files
# import os

# # pwd - print the current working directory
# print("Current working directory:", os.getcwd())


# # File paths

# TEXT_FILE_NAME = "data.txt"

# file_path = os.getcwd() + '/' + TEXT_FILE_NAME

# # May not work across all OSs
# # Using os.path.join helps put here
# # BETTER!
# file_path = os.path.join(os.getcwd() + '/' + TEXT_FILE_NAME)

# print(file_path)

from pathlib import Path

# Get the current working directory
current_dir = Path.cwd()

# Define the text file name
TEXT_FILE_NAME = "demo_files/data.txt"

# Create the full file path
# file_path = current_dir / TEXT_FILE_NAME

# print(file_path)

# # Check if a file exists

# # if(os.path.exists(file_path)):
# #   print("File exists!")

# if (Path.exists(file_path)):
#     print("File exists!")
# else:
#     print("File not found!")

# # Make a new directory

# new_directory_path = current_dir / "new_directory"

# new_directory_path.mkdir(exist_ok=True)
# # prevent any errors if the directory already exists

# # Opening a file
# opened_file = open(file_path)
# # print(opened_file)

# with open(file_path) as file:
#     # Do stuff with the file contents
#     print(file.read())

# # context manager automatically closes the file
# # when the block of code is exited - no more reads allowed
# # print(file.read())
# opened_file = open(file_path)
# print(opened_file.read())
# opened_file.close()
# # print(opened_file.read())

# text file path

text_file_path = current_dir / TEXT_FILE_NAME

# Just iterates over all lines in the file
# Good for getting all data in one go
with open(text_file_path) as text_file:
    for line in text_file:
        print(line.strip())

# Reads a single line and stops
# Does some action and then reads in the next line
# When the line is empty, it breaks from the while loop
# Good for real-time processing of each line
with open(text_file_path) as text_file:
    line = text_file.readline()
    while line:
        print(line.strip())
        if 'swear word' in line:
            break
        line = text_file.readline()
