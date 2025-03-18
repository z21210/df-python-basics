from pathlib import Path

cwd = Path.cwd()

demo_file_path = cwd / 'demo_files' / 'my_data.txt'


# file = open(demo_file_path)

"""
This will cause an Exception if the file is not found
Which means the script stops executing!
"""

file = None # Initialise the file variable

try:
    # break_time = False
    # question = "Is it break time yet?"
    # answer = question + break_time
    file = open(demo_file_path)
# except TypeError as te:
#     print(f'TypeError: {te}')
except FileNotFoundError as fnf:
    print(f'FileNotFoundError: {fnf}')
except OSError as e:
    print(f'OSError: {e}')
except Exception as e:
    print(f'Exception: {e}')
finally:
    if file: # Check if files exists and is open
        file.close()
        print("File closed")
    print("Continuing the program...")

"""
Exceptions need to be handled from the most specific at the top
to least specific at the bottom - remember the shape analogy!
try should only contain the code that is likely to produce the exception.
Otherwise you risk not executing some parts of the code!
The finally block is often used for cleaning up - nulling values,
closing files/database connections etc
"""
