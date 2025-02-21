# Debugging

## Aims

The aims of this lesson are to provide an introduction into debugging code, giving strategies and tooling to make the process educational and efficient.

---

## Learner Stories

```text
As a DATA PROFESSIONAL,  
I want to be able to write UNIT TESTS using the `unittest` and/or `pytest` module,  
so that I can ENSURE my CODE is RELIABLE and WORKS correctly

As a DATA PROFESSIONAL,  
I want to be able to use debugging tools like `pdb` to set breakpoints and step through my code,  
so that I can identify and fix bugs effectively
```

---

## Definition of DONE

- [ ] The data professional has completed a tutorial or training session on writing unit tests in Python using `unittest` and/or `pytest`, focusing on their syntax and features.
- [ ] The data professional can explain the purpose of unit testing, the differences between `unittest` and `pytest`, and how to write effective test cases.

The data professional has written unit tests demonstrating:

- [ ] Creating and organising test cases using `unittest` with `TestCase` classes, and using assertions to validate code behaviour.
- [ ] Writing tests using `pytest` with simple function-based test cases and fixtures for `setup` and `teardown`.
- [ ] Running and interpreting test results from both `unittest` and `pytest`.
- [ ] Implementing *parameterised* tests and *mocking* dependencies where needed.

The data professional has completed exercises that demonstrate:

- [ ] Writing comprehensive test cases for different types of functions and scenarios (e.g., edge cases, expected failures).
- [ ] Integrating unit tests into a development workflow, including running tests automatically during development or deployment.

- [ ] Code reviews have been conducted for these tests, confirming that tests are comprehensive, correctly implemented, and follow best practices.
- [ ] The data professional has created a set of unit tests for a script or module, demonstrating thorough testing and validation of the code’s functionality.
- [ ] All tests are organised and documented according to best practices for unittest and pytest.
- [ ] Tests have been successfully executed using unittest and/or pytest, with clear and accurate reporting of test results.
- [ ] The data professional has completed a quiz or assessment on unit testing and test frameworks and passed with a score of at least 80%.
- [ ] Examples of unit tests written using unittest and/or pytest are documented in a shared knowledge repository or personal learning journal.
- [ ] Feedback from peers or mentors on unit testing practices has been reviewed, and any suggested improvements have been implemented.

---

## Debugging Connections

**Questions:**

> What is debugging?
> What types of bugs might you find?

**Timebox:** 5 minutes

---

## Debugging Concepts

### Discussion Points

- How do we identify bugs?
- How do we go about resolving them?

### Debugging Nomenclature

> All great debuggers are great programmers, but not all programmers are great debuggers.

Debugging literally means 'removing bugs'. The name comes from a story about the computing pioneer Grace Hopper [Who is Grace Hopper](https://en.wikipedia.org/wiki/Grace_Hopper), who once tracked down a problem to a literal bug, taping it to her report for good measure:

![Image of a moth attached to a bug log](https://i.imgur.com/bs71qW0.png)

You can see from the above page that Hopper was following a methodical process.

Many bugs will be so easy you don't even notice yourself fixing them. But most of the *time* you spend debugging will be on the hard bugs. And most of your time spent programming will be spent debugging.

As such, it makes a lot of sense to develop your debugging skill. The more you improve that skill, the faster you are to extract the learning from the experience and move on to the next.

Let's consider two mindsets, 'brain modes', we might use to find bugs:

1. Find the fix
2. Find the problem

When **finding the fix** we're solution-oriented. We're driven to try the first thing we see in hope it works.

When **finding the problem** we're learning-oriented. We're driven to understand the code we look at before we make changes.

Most people instinctively jump to the fixing mindset, because in the real world we can often merely 'look for something out of place' in order to fix problems.

It's actually a pretty good strategy in most situations — but not for the hard bugs.

---

The biggest tool in our armoury is **getting visibility**.

You'll hear this term a lot. It refers to a variety of techniques to 'see into' your program as it runs. This helps us understand the code.

Consider this buggy example:

```python
def factorial(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1
    return product

# Expected output:
#
# > factorial(5)
# => 120

print(factorial(5))  # => 120
```

We could comb through the code, keep everything in our heads and figure out what is wrong with it, or we could **get visibility** and ask the program to tell us using `print()`, like so:

```python
def factorial(n):
    product = 1
    print(f"at the start: product is {product}")
    while n > 0:
        n -= 1
        print(f"we multiply: {product} by {n}")
        
        product *= n
        
        print(f"we get: {product}")
    return product

# Example usage
factorial(5)
```

Try running that and fixing the bug.

---

### Additional Resources

- [Debugging in an IDE](https://code.visualstudio.com/docs/editor/debugging)
  - Most IDEs have debugging capability.
  - Once you can master one, you'll be able to adapt to many.
  - VSCode has debugging capability for most languages - here are the specific instructions for [Python in VSCode](https://code.visualstudio.com/docs/python/debugging).
  - Read about it by clicking the link above (it will open in a new tab).

---

## 3. Concrete Practice

Your trainer will assign you to a Zoom breakout room to work with at least one other.

## Activity 1

Debug this:

```python
def sayHi(name):
    print(f'Hi, {name}!"')

// expected output:
//
// > sayHi("Ed")
// => "Hi, Ed!"
```

You should look to be able to track the value of `name` as it executes.

---

## Activity 2

Debug this:

```python
import os

char_set = {}

def encode(string, key):
    return ''.join([
        str((int(char_set[char]) + key) % 99).zfill(2)
        for char in string
    ])

def parse_character_set(data):
    result = {}
    for line in data.split('\n'):
        if line.strip():
            char, number = line.split(',')
            result[char] = number
    return result

def main():
    try:
        with open('char-set.txt', 'r', encoding='utf8') as file:
            data = file.read()
            global char_set
            char_set = parse_character_set(data)
            print(encode('Hi, mse-2103-a!', 4))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

# Expected console output => '391482051824106893920294680658'

```

You need to work out how this program works and passes data to get to the result.

---

## Activity 3

```python
import os

char_set = {}

def encode(string, key):
    return ''.join([
        str((int(char_set[char]) + key) % 99).zfill(2)
        for char in string
    ])

def parse_character_set(data):
    result = {}
    for line in data.split('\n'):
        if line.strip():
            char, number = line.split(',')
            result[char] = number
    return result

def main():
    try:
        with open('char-set.txt', 'r', encoding='utf8') as file:
            data = file.read()
            global char_set
            char_set = parse_character_set(data)
            print(encode('Hi, mse-2103-a!', 4))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

# Expected console output => '391482051824106893920294680658'
```

This code is broken.

Your task is **not** to fix this code. Let go of that idea.

Imagine your friend wrote this code and doesn't know where he went wrong. He doesn't need your fix — he needs to understand the problem so he can write better code.

You're a code archaeologist now!

The code for the character set is in the file **char-set.txt**. You need to create this file from the text in the [appendix](#appendix) of this document.

---

## Activity 4

The file **char-set.txt** should be created from the text in the [appendix](#appendix) of this document.

Debug this:

```python
import os

char_set = {}

def decode(string, key):
    inverted_char_set = invert(char_set)
    return ''.join([
        inverted_char_set[str((99 + (int(''.join(pair)) - key)) % 99)]
        for pair in chunk(list(string), 2)
    ])

def chunk(array, chunk_size):
    return [array[i:i + chunk_size] for i in range(0, len(array), chunk_size)]

def invert(obj):
    return {value: key for key, value in obj.items()}

def parse_character_set(data):
    result = {}
    for line in data.split('\n'):
        if line.strip():
            char, number = line.split(', ')
            result[char] = number
    return result

def main():
    try:
        with open('char-set.txt', 'r', encoding='utf8') as file:
            data = file.read()
            global char_set
            char_set = parse_character_set(data)
            print(decode('391482051824106893920294680658', 4))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

# Expected console output => 'Hi, mse-2103-a!'

```

**Timebox:** 30 minutes

### Bonus

Your trainer may demonstrate how the debugger in ***VSCode*** could have been used to debug this program.

---

## 4. Debugging - Conclusions

- The debugging process is a skill that can be learned and improved over time.
- Debugging is about finding the problem, not just the fix.
- Getting visibility into your code is crucial for understanding and fixing bugs.
- Debugging tools like print statements and IDE debuggers can help you identify and resolve issues in your code.
- Practice and experience are key to becoming a proficient debugger.

---

## Appendix

The following is to be put into the file `char-set.txt` and saved to the same location as your Python files for the activities.

```text
character, value
 , 1
a, 2
b, 3
c, 4
d, 5
e, 6
f, 7
g, 8
h, 9
i, 10
j, 11
k, 12
l, 13
m, 14
n, 15
o, 16
p, 17
q, 18
r, 19
s, 20
t, 21
u, 22
v, 23
w, 24
x, 25
y, 26
z, 27
A, 28
B, 29
C, 30
D, 31
E, 32
F, 33
G, 34
H, 35
I, 36
J, 37
K, 38
L, 39
M, 40
N, 41
O, 42
P, 43
Q, 44
R, 45
S, 46
T, 47
U, 48
V, 49
W, 50
X, 51
Y, 52
Z, 53
!, 54
@, 55
£, 56
$, 57
%, 58
^, 59
&, 60
*, 61
(, 62
), 63
-, 64
_, 65
=, 66
+, 67
[, 68
], 69
{, 70
}, 71
;, 72
:, 73
', 74
", 75
\, 76
|, 77
,, 78
., 79
<, 80
>, 81
/, 82
?, 83
`, 84
~, 85
§, 86
±, 87
1, 88
2, 89
3, 90
4, 91
5, 92
6, 93
7, 94
8, 95
9, 96
0, 97
```
