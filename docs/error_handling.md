# Error Handling

## Aims

The aims of this lesson are look at ways that we can anticipate and gracefully handle errors in our code.  We will look at how to use the `try` and `except` blocks to catch errors and prevent our program from crashing.  We will also look at how to use the `finally` block to run code that should always run, regardless of whether an error occurs.

---

## Learner Stories

```text
As a DATA PROFESSIONAL,  
I want to be able to IMPLEMENT ERROR HANDLING using TRY and EXCEPT BLOCKS,
  so that I can CATCH and MANAGE RUNTIME ERRORS effectively, ensuring my scripts are ROBUST and RELIABLE

As a DATA PROFESSIONAL,  
I want to be able to understand COMMON EXCEPTIONS and how to HANDLE THEM,  
so that I can PREVENT my SCRIPTS from CRASHING unexpectedly
```

---

## Definitions of DONE

### Story 1

- [ ] The data professional has completed a tutorial or training session on error handling in Python, focusing on try, except, finally, and else blocks.
- [ ] The data professional can explain the purpose and structure of error handling in Python and how it helps manage runtime errors and improve script reliability.

The data professional has written scripts demonstrating:

- [ ] Basic error handling using try and except to catch and handle common exceptions (e.g., FileNotFoundError, ValueError).
- [ ] Using the else block to define code that runs if no exceptions are raised.
- [ ] Using the finally block to define code that always executes regardless of whether an exception occurred.
- [ ] Handling multiple exceptions in a single try block.

The data professional has completed exercises that demonstrate:

- [ ] Creating custom exceptions by defining custom exception classes.
- [ ] Raising exceptions intentionally using the raise keyword.
- [ ] Logging errors using Python’s logging module within except blocks.

- [ ] Code reviews have been conducted for these scripts, confirming correct implementation of error handling and adherence to best practices.
- [ ] The data professional has created a script that demonstrates robust error handling in a real-world data processing scenario, ensuring the script can handle unexpected situations gracefully.
- [ ] All scripts are formatted according to PEP 8 guidelines and adhere to Python best practices.
- [ ] All scripts have been successfully executed in a Jupyter Notebook environment, with correct handling of errors and expected outputs.
- [ ] The data professional has completed a quiz or assessment on error handling and passed with a score of at least 80%.
- [ ] Examples of error handling using try and except are documented in a shared knowledge repository or personal learning journal.
- [ ] Feedback from peers or mentors on error handling practices has been reviewed, and any suggested improvements have been implemented.

### Story 2

- [ ] The data professional has completed a tutorial or training session on Python exceptions, focusing on common exception types and handling techniques.
- [ ] The data professional can explain the purpose of handling exceptions and list common Python exceptions such as FileNotFoundError, ValueError, IndexError, KeyError, and TypeError.

The data professional has written scripts demonstrating:

- [ ] Handling specific common exceptions using try and except blocks.
- [ ] Using multiple except clauses to handle different types of exceptions.
- [ ] Implementing fallback mechanisms or default actions when exceptions occur.

The data professional has completed exercises that demonstrate:

- [ ] Identifying potential sources of common exceptions in a script and adding appropriate error handling.
- [ ] Writing code that includes meaningful exception messages to aid in debugging and troubleshooting.
- [ ] Using else and finally blocks in conjunction with try and except for comprehensive error handling.

- [ ] Code reviews have been conducted for these scripts, confirming that common exceptions are handled correctly and that error handling improves script stability.
- [ ] The data professional has created a script that demonstrates handling common exceptions in a real-world data processing scenario, ensuring the script does not crash unexpectedly.
- [ ] All scripts are formatted according to PEP 8 guidelines and adhere to Python best practices.
- [ ] All scripts have been successfully executed in a Jupyter Notebook environment, with correct handling of common exceptions and expected outputs.
- [ ] The data professional has completed a quiz or assessment on common exceptions and exception handling, and passed with a score of at least 80%.
- [ ] Examples of handling common exceptions are documented in a shared knowledge repository or personal learning journal.
- [ ] Feedback from peers or mentors on exception handling practices has been reviewed, and any suggested improvements have been implemented.

---

## Introduction

Error handling is a way to deal with errors that might occur in your code. It is a way to prevent your program from crashing when an error occurs.  It allows your program to recognise that something has gone wrong and respond to it in a way that you define.  This can be particularly useful when you are working with user input, as you can anticipate that the user might enter something unexpected.  It is also useful when working with network connections or files that might not be available.  In this section, we will look at how to use error handling in Python.

## Syntax

The syntax for error handling in Python is as follows:

```python
try:
    # code that might raise an error
except ErrorType:
    # code to run if an error of type ErrorType occurs
```

The `try` block contains the code that might raise an error.  If an error occurs, the program will jump to the `except` block.  The `except` block contains the code that should run if an error occurs.  The `ErrorType` is the type of error that you are expecting.  You can specify the type of error that you are expecting, or you can use a general `except` block to catch any error.

## Example

In the following example, we will try to open a file that does not exist.  We will use error handling to catch the error that occurs when the file does not exist.

```python
try:
    file = open("file.txt", "r")
except FileNotFoundError:
    print("File not found")
```

In this example, we try to open a file called `file.txt` in read mode.  If the file does not exist, a `FileNotFoundError` will be raised.  We use error handling to catch this error and print a message to the console.

---

## Different Error Types

Python has a number of built-in error types that you can use to catch specific errors.  Some of the most common error types are:

- `FileNotFoundError`: Raised when a file is not found
- `TypeError`: Raised when an operation is performed on an object of an inappropriate type
- `ValueError`: Raised when a function receives an argument of the correct type, but with an inappropriate value
- `ZeroDivisionError`: Raised when division or modulo by zero is performed
- `IndexError`: Raised when an index is out of range
- `KeyError`: Raised when a key is not found in a dictionary
- `NameError`: Raised when a local or global name is not found
- `SyntaxError`: Raised when there is a syntax error in the code
- `IndentationError`: Raised when there is an incorrect indentation in the code
- `AttributeError`: Raised when an attribute reference or assignment fails
- `ImportError`: Raised when an import statement fails
- `ModuleNotFoundError`: Raised when a module is not found

You can use these error types to catch specific errors in your code and catch different types from the same `try` block.

For example, you can catch a `FileNotFoundError` and a `ValueError` in the same `try` block:

```python
try:
    file = open("file.txt", "r")
    value = int("abc")
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid value")
```

In this example, we try to open a file called `file.txt` in read mode and convert the string `"abc"` to an integer.  If the file does not exist, a `FileNotFoundError` will be raised.  If the string cannot be converted to an integer, a `ValueError` will be raised.  We use error handling to catch these errors and print a message to the console.

---

## The `finally` Block

You can use a `finally` block to run code that should always run, regardless of whether an error occurs.  The `finally` block is optional and is placed after the `except` block.

```python
try:
    file = open("file.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file")
    file.close()
```

In this example, we try to open a file called `file.txt` in read mode.  If the file does not exist, a `FileNotFoundError` will be raised.  We use error handling to catch this error and print a message to the console.  We then use a `finally` block to close the file, regardless of whether an error occurs.

`try:except` can also be used within a ***context manager***:

```python
with open("file.txt", "r") as file:
    try:
        # code that might raise an error
    except ErrorType:
        # code to run if an error of type ErrorType occurs
```

In this case, the `finally` block is not needed, as the file will be closed automatically when the `with` block exits.
