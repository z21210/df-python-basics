# Exercise 1 Solution:

file1 = 'data.txt'                   # will raise FileNotFoundError
# file1 = 'demo_files/data.txt'      # should print the file contents

try:
    with open(file1, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'data.txt' was not found.")

# Exercise 2 Solution:
# This file will automatically be created in the current directory 
# if it does not exist!

lines = [
    "Line 1: Hello, world!",
    "Line 2: Python file handling.",
    "Line 3: Goodbye!"
]

with open('output.txt', 'w') as file:
    for line in lines:
        file.write(line + "\n")

# Exercise 3 Solution:
# You will need to create the text file for this exercise!

try:
    with open('protected.txt', 'w') as file:
        file.write("This is a test.")
except PermissionError:
    print("Error: You do not have permission to write to 'protected.txt'.")

# Exercise 4 Solution:

file4 = 'data_with_error.csv'                # will raise FileNotFoundError
# file4 = 'demo_files/data_with_error.csv'     # will raise ValueError

try:
    with open(file4, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'data.csv' was not found.")
except ValueError:
    print("Error: There was a problem reading the file content.")

# Exercise 5 Solution:

file5 = None
try:
    file5 = open('demo_file/data.txt', 'r')
    content = file5.read()
    print(content)
except FileNotFoundError:
    print("Error: The file 'log.txt' was not found.")
finally:
    if file5:
        file5.close()

try:
    print(file5)
except NameError:
    print("Error: The file object 'file' is not defined.")

# Exercise 6 Solution:

file6 = 'demo_files/data.txt'

with open(file6, 'a') as file:
    file.write("New entry\n")

# Exercise 7 Solution:

file7 = 'demo_files/data.txt'

try:
    with open(file7, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'data.txt' was not found.")
except PermissionError:
    print("Error: You do not have permission to access 'data.txt'.")
