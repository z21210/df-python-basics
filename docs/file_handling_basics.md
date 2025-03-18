# File Handling Basics

## Aims

The aims of the section are to introduce the basics of file handling in Python, focussing on the local file system.  We will cover how to access and construct paths to files, how to open and close files, and how to read and write to files.

---

## Learner Stories

```text
As a DATA PROFESSIONAL,  
I want to be able to READ from and WRITE to FILES in VARIOUS FORMATS,  
so that I can INGEST DATA from DIFFERENT SOURCES and OUTPUT RESULTS for further use

As a DATA PROFESSIONAL,  
I want to be able to use CONTEXT MANAGERS (with statements) when HANDLING FILES,  
so that I can MANAGE RESOURCES SAFELY and AVOID DATA CORRUPTIONS or FILE LOCKS
```

---

## Definitions of DONE

### Story 1

- [ ] The data professional has completed a tutorial or training session on file handling in Python, including reading from and writing to files in various formats (e.g., CSV, JSON, TXT).
- [ ] The data professional can explain the different file formats and their use cases, including advantages and limitations of each format.

The data professional has written scripts demonstrating:

- [ ] Reading data from CSV files using Python’s built-in csv module or libraries like pandas.
- [ ] Writing data to CSV files using Python’s built-in csv module or libraries like pandas.
- [ ] Reading from and writing to JSON files using Python’s json module.
- [ ] Handling plain text files (e.g., reading from and writing to .txt files).

The data professional has completed exercises that demonstrate:

- [ ] Reading large files efficiently (e.g., using chunking or streaming).
- [ ] Writing formatted data to files (e.g., handling delimiters, line endings).

- [ ] Code reviews have been conducted for these scripts, confirming correct implementation of file I/O operations and adherence to best practices for file handling.
- [ ] The data professional has created a script that demonstrates the end-to-end process of reading data from a file, processing it, and writing results to another file.
- [ ] All scripts are formatted according to PEP 8 guidelines and adhere to Python best practices.
- [ ] All scripts have been successfully executed in a Jupyter Notebook environment, and file operations work as expected without errors.
- [ ] The data professional has completed a quiz or assessment on file handling and passed with a score of at least 80%.
- [ ] Examples of file handling operations are documented in a shared knowledge repository or personal learning journal.
- [ ] Feedback from peers or mentors on file handling practices has been reviewed, and any suggested improvements have been implemented.

### Story 2

---

## File Handling in Python

Python provides basic functions and methods necessary to manipulate files by default. You can do most of the file manipulation using a file object.

### The `os` Module

The importable `os` module in Python provides a way of using operating system dependent functionality. The functions that the OS module provides allows you to interface with the underlying operating system that Python is running on – be that Windows, Mac or Linux.

```python
import os
```

---

### Finding the Current Working Directory

You can get the current working directory using the `os` module.

```python
import os

# Get the current working directory
cwd = os.getcwd()
print(cwd)
```

---

### Constructing File Paths

The `os.path` module provides a way of working with file paths. You can use the `os.path.join()` method to construct file paths.

```python
import os

# Construct a file path
file_path = os.path.join("C:", "Python38", "README.txt")
print(file_path)
```

---

### Checking if a File Exists

You can use the `os.path.exists()` method to check if a file exists.

```python
import os

# Check if a file exists
file_path = os.path.join("C:", "Python38", "README.txt")
if os.path.exists(file_path):
    print("File exists")
else:
    print("File does not exist")
```

---

### Creating a Directory

You can use the `os.mkdir()` method to create a directory.

```python
import os

# Create a directory
os.mkdir("test")
```

---

## The `open()` Function

Before you can read or write a file, you have to open it using Python's built-in `open()` function. This function creates a file object, which would be utilized to call other support methods associated with it.

```python
f = open("test.txt")    # open file in current directory

f = open("C:/Python38/README.txt")  # specifying full path
```

### The `open()` Function Modes

The `open()` function takes two parameters; filename, and mode.

- `r`: Opens a file for reading. (default)
- `w`: Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
- `x`: Opens a file for exclusive creation. If the file already exists, the operation fails.
- `a`: Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
- `t`: Opens in text mode. (default)
- `b`: Opens in binary mode.
- `+`: Opens a file for updating (reading and writing)

```python
f = open("test.txt")       # equivalent to 'r' or 'rt'
f = open("test.txt", 'w')  # write in text mode
f = open("img.bmp", "r+b") # read and write in binary mode
```

---

### Closing a File

When you're done with a file, it is good practice to close it.

```python
f = open("test.txt")
f.close()
```

---

### Context Managers

It is good practice to use the `with` keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point.

```python
with open("test.txt") as f:
    # perform file operations
```

Here the `with` keeps the file open within the block of code and we can reference it as `f` due to the `as` keyword. Once the block of code is executed, the file is automatically closed.

This is the simplest way to use a ***Context Manager***.  Behind the scenes use in-built functions `__enter__` and `__exit__` to open and close the file.  You can create your own versions of context managers using these functions.

```python
class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

# Usage:
with MyContextManager() as cm:
    print("Inside the context")
```

---

## Reading Files

You have options! You can either read the entire file at once, or you can read it line by line.  The choice here may well depend on the size of the file you are working with.  Larger files may be more efficiently processed line by line.

### Reading Entire Files

You can read the contents of a file using the `read()` method.

```python
with open("test.txt") as f:
    content = f.read()
    print(content)
```

---

### Reading Files Line-by-Line

You can read the contents of a file line by line using the `readline()` method.

```python
with open("test.txt") as f:
    for line in f:
        print(line, end="")
```

---

## Activities

### Exercise 1: Reading a File with try:except

***Objective:*** Read the content of a file and handle the case when the file doesn’t exist.

1. Create a Python script that attempts to open and read from a file called `data.txt`.
2. If the file doesn’t exist, catch the `FileNotFoundError` and print an error message.
3. Verify that the script works by running it whilst pointing to the wrong path for the file.
4. Correct the file path and run the script again to ensure it reads the file content.

---

### Exercise 2: Writing to a File with Context Manager

***Objective:*** Write data to a new file using a context manager.

1. Create a Python script that writes the following list to a file called `output.txt` using a ***context manager:***

`lines = ["Line 1: Hello, world!", "Line 2: Python file handling.", "Line 3: Goodbye!"]`

2. After running the script, check if the file `output.txt` has been created with the correct content.

---

### Exercise 3: Handling Permission Errors with `try:except`

***Objective:*** Handle permission errors when trying to write to a file.

 1. Create a Python script that attempts to write to a file called `protected.txt`.
 2. Ensure that if the script doesn’t have permission to write to the file (e.g., due to file permissions), a `PermissionError` is caught and an error message is printed.

> Tip: Change the file permissions to read-only to test the script use your terminal or GitBash and command: `chmod 400 protected.txt` from the same folder where the file is located.

---

### Exercise 4: Safe File Handling with Context Manager and `try:except`

***Objective:*** Use both a context manager and a try:except block to handle both file reading and potential errors.

 1. Create a Python script that attempts to read a file called data.csv.
 2. Use a context manager to safely open the file, and use a `try:except` block to catch potential errors like `FileNotFoundError` and `ValueError`.
 3. Print a message for each type of error.

---

### Exercise 5: Ensure File Closure with finally

***Objective:*** Ensure the file is properly closed using the finally block after attempting to open a file.

 1. Create a Python script that attempts to open and read a file called `data.txt`.
 2. Ensure that the file is properly closed using the finally block (try to access it again after the script has run to verify it is closed).

> DO NOT USE A `with` STATEMENT FOR THIS EXERCISE!

---

### Exercise 6: Use a Context Manager to Safely Append to a File

***Objective:*** Safely append content to a file using a context manager.

 1. Create a Python script that appends the text `"New entry"` to a file called `log.txt`.
 2. Use a context manager to ensure the file is properly closed after the operation.

---

### Exercise 7: Combine `try:except` and Context Manager for Error Handling

***Objective:*** Use both `try:except` and ***context managers*** together for robust error handling.

 1. Create a Python script that attempts to open a file called `data.txt` and read its content.
 2. Handle potential `FileNotFoundError` and `PermissionError` exceptions.
 3. Use a *context manager* to ensure the file is properly closed after reading.

---

### Key Points for Learners

- `try:except` blocks help handle errors and prevent your program from crashing unexpectedly.
- Context managers (using with statements) automatically manage resource clean up, ensuring files are properly closed after usage.
- `finally` block ensures that clean up actions, like closing files, are always executed, even if an error occurs.
