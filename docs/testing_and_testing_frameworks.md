# Testing and Testing Frameworks

## Overview

There are many different practices and techniques used to develop software.  All have their own merits, advantages and disadvantages.   This course will help you develop a simple testing framework to help test your code produces the expected outcomes.

---

## Aims

The aim of this section is to allow you begin to explore different ways of developing and testing software so that you can appreciate the need for the thorough testing of code, the ways in which tests can be administered and how bugs can be identified and fixed.

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

## Definitions of DONE

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

## Testing and Test Frameworks - Connections

> Why is it important to test code?
> What are the characteristics of a good test?

---

## Testing and Test Frameworks - Concepts

### Testing Overview

Testing is important as it increases the quality of the code. This means it is less likely to break when it has been deployed and it is being used.

Well-written tests tell the development team exactly where an issue is in the code base, explain what the issue is and even what caused the issue. This means that less time is spent debugging and fixing code that has already been written.

Sometimes, when new functionality is added that interacts with existing code, it is possible that old previously working code stops working. Testing in a deployment pipeline is crucial to this - before any new code is merged to the production branch, it should go through all previous tests to make sure that nothing is broken. If extensive testing isn't completed before new code is merged in, then it is probable at some point it will break the software, as in this example:

> On June 4th, 1996, the very first Ariane 5 rocket seemingly inexplicably self-destructed.  The fault was quickly identified as a software bug in the rocket’s Inertial Reference System - [read more here](https://www.bugsnag.com/blog/bug-day-ariane-5-disaster)

It is a common misconception that a Testers job is to test the code written by the developers. Usually testers will test the system as a whole and developers should write tests for the code that is written. Testers can lend expertise on what the developers should be testing, but the responsibility relies on the development team.

## Types of Testing

There are several different types of test that can be run on software.  All have their benefits.

### Unit Testing vs Component Testing vs Integration Testing

#### Unit Testing

- Ensures all of the features within the Unit (class) are correct
- Dependent/Interfacing units are typically replaced by stubs, simulators or trusted components
- Tools that allow component mocking/simulation are often used

#### Component Testing

- Similar to Unit testing but with a higher level of integration between units
- Units within component are tested as together real objects
- Dependent components can be mocked

#### Integration Testing

- Involves the testing of two or more integrated components
- Can also mean the testing of the integration of different systems used in a more complex one (known as end-to-end)

### Functional Testing vs Non-Functional Testing

Functional testing is primarily focused on how code is structured, compiled, and runs. If there is a value being returned that doesn't meet our expectations, we might want to know precisely where this is happening and why.

Non-functional testing aims to identify issues with the required operation objectives. In contrast to functional testing, non-function requirements focus on system readiness rather than specific behaviors. These objectives include things like maintainability or ease of use, the goal is to reduce risk or costs. Given the difficulty of carrying out certain Non-functional tests manually, there is a wide range of tools that allow testers to automate some of the more unfeasible.

---

## Edge and Corner Cases

**Edge Testing:** Imagine you have a piece of paper. The edges of that paper are the outer limits, right? In software, the "edges" are like the boundaries or limits of what the software can do. So, edge testing is checking how the software behaves right at those limits.

**Example:** Let's say you have a game where players can score points, and the maximum score allowed is 100. Edge testing would involve checking what happens when a player tries to score exactly 100 points. Does the game handle it correctly, or does it have a problem?

**Corner Testing:** Now, think about the corners of that paper. They are where two edges meet. In software, the "corners" are where different limits come together. So, corner testing is about checking what happens when you're at the intersection of multiple limits.

**Example:** Imagine you have an app that lets you set reminders, and it allows you to set a maximum of 10 reminders. Corner testing would involve checking what happens when you try to set the 10th reminder at the exact moment the app is running out of memory. It's like being in the corner where the number of reminders meets the memory limit.

In a nutshell, edge testing is about checking the limits, and corner testing is about checking what happens when you're at the meeting point of different limits. Both help make sure the software works well in all situations!

---

### Unit Testing in more detail

#### What are Unit Tests?

- A software testing method written in code where individual sections of code are tested.
- We refer to a unit as the smallest testable part of the software under test.
- Allows us to test bits of code in isolation.
- Can be written before the code to be tested (known as TDD).
- They are automated.
- Tiny pieces of code that developers write, execute and maintain.

#### Benefits of Unit Testing

- As they test our code, shows us if our code really works
- Saves a lot of time later down the line
  - Helps prevent code later down the line not function how it should
- Deployment is a lot easier
  - We can use continuous integration (CI) to run our tests, pull down latest changes, push code to a remote repository
- Detects defects early on – software bugs found early
- Improves the quality of our code
- Simplifies the debugging process
- Localise the source of the bug more easily

### Structure of a Unit Test

Tests should be coded consistently with a well defined clear intent.

Four phases are standard:

#### Setup / Arrange

- Setup the initial state for the test

#### Exercise / Act

- Perform the action under test

#### Verify / Assert

- Determine and verify the outcome

#### Clean Up

- Clean-up the state created

Each phase should be:

- Clearly Expressed
- Well documented

Expected Outcomes should be clearly expressed

---

### Test Code Example

```python
# test_testing_and_testing_frameworks.py

import pytest

def count_even_numbersInArray(arr):
    return len([x for x in arr if x % 2 == 0])

def test_count_even_numbersInArray():
    # Setup/Arrange
    input = [1, 2, 3, 4, 5, 6]
    expected_output = 3

    # Execute/Act
    actual_output = count_even_numbersInArray(input)

    # Verify/Assert
    assert actual_output == expected_output

if __name__ == "__main__":
    pytest.main()
```

---

### Acceptance Criteria

We have this specification:

```sh
Write a program that you can run that can find how many even numbers are in a list of numbers

# Acceptance Criteria
Input => Output
[1,2,3,4,5,6] => 3
[0,1,2] => 2
[1,3,5] => 0
```

#### What are **Acceptance Criteria**?

They define success for those implementing and testing. They can be written in different ways, sometimes very specific and at other times vague.

You know you have completed the initial implementation once you've met the criteria. However, better implementations will sometimes mean defining more criteria, sometimes breaking them down into simpler steps, at other times adding your own steps to help drive development. If you're in doubt about whether your added acceptance criteria are valid, check with the owner of the requirements - in this case usually a coach!

We'll give you requirements and acceptance criteria for the most part, but it will be your job to clarify them or define and refine them from the information you're given.

The great thing about using or defining ***Acceptance Criteria*** is that you can quickly convert them into your first tests!

---

### Test Frameworks

To be able to repeat tests (and by extension, add them to automated processes), we need some sort of Framework that will provide the rules and environment for running the tests and they also provide a number of "helper" functions such as assert_equals.  They can usually be extended and there are many different test frameworks for each programming language.

#### The xUnit Frameworks

These are based on the original SUnit framework, developed for a programming language called SmallTalk.

Most commonly these are:

- **JUnit** — Unit testing framework for Java code.
- **NUnit** — Unit testing framework for C#, VB.NET, and other .NET language code.
- **CppUnit** — Unit testing framework for C++ code.
- **PyUnit** — Unit testing framework for Python code ***aka unittest***

#### Other Frameworks

The xUnit frameworks are not the only test frameworks out there.  Each language has many!  This [Wikipedia](https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks) page lists them.

- **Behave** - good for [BDD](https://en.wikipedia.org/wiki/Behavior-driven_development) (Behaviour Driven Development)
- **Robot** - good for acceptance testing
- **pytest** - the most popular Python testing framework

#### Assertion Libraries

One of the most useful thing about test frameworks is the fact that they usually provide an ***Assertion Library***.  These are sets of functions that allow you to compare expected outputs with actual outputs in a manner of ways.  They usually return a boolean value.

An example of an `assert_equals` function (in JavaScript):

```python
def assert_equals(expected_output, actual_output):
    return expected_output == actual_output
```

So in this case, if we were to call this function, supplying the same value as `expected_output` and `actual_output` it would return `true`:

```python
value1 = 10;
value2 = 10;
result = assert_equals(value1, value2);  # Sets result to true
```

This is a simple assertion function, more complex ones exist and are dependent on the framework.

---

### Summary

You will find that most of these frameworks work, language-independently, in the same way.  Once you master how to write a good test, its a case of applying the correct syntax for the language and framework you are using.

---

### Additional Resources

[Characteristics of Good Tests](https://www.codecademy.com/articles/tdd-u1-good-test)

---

## Testing and Test Frameworks - Concrete Practice

Work through the instructions below.

## Activity 1 - Test Framework

- [ ] Create a new directory for this project
- [ ] Create a file for your test framework inside the project folder
- [ ] Write a method that returns a boolean from comparing two values
- [ ] Write some code to call your test framework with some values to check that the method works
- [ ] Run your test framework file - if the outputs are correct, delete the method calls (but not the `assert_equals`!)

***Hint/Solution:***

<details>

You probably implemented something like this:

```python
# testing_framework.py
def assert_equals(val1, val2):
    return val1 == val2
```

You can now import this file to have access to our `assert_equals()` method in order to test that two values are equal to each other. This gives us a simple way to write tests for the programs we want to write.

</details>

## Example

> Write a program that you can run in node that can find how many numbers are even in a list of numbers

### Activity 1 Acceptance Criteria

```sh
Input => Output
[1,2,3,4,5,6] => 3
[0,1,2] => 2
[1,3,5] => 0
```

The first step to write a test for the program we need to implement, based on acceptance criteria. Read the below stages of setting up a test:

```python
# 1. Arrange
from testing_framework import assert_equals

input = [1,2,3,4,5,6]
expected_output = 3

# 2. Act
actual_output = count_even_numbers(input)

# 3. Assert
result = assert_equals(actual_output, expected_output)
print(result)
```

1. **IMAGINE:** This step is important and can be tricky when picking up the TDD mindset: we haven't yet written any source code, and yet we're *imagining what the method is going to look like.* We're saying to ourselves we are going to define a method called `count_even_numbers` and when we call it with the argument `[1,2,3,4,5,6]` we want it to return `3`.

2. **ORGANISE:** There are [4 phases](https://thoughtbot.com/blog/four-phase-test) to tests. We won't worry about the 4th phase for now. Get into the habit of organising your tests into these phases - some stages may happen together.

What's the difference between specs and tests? You'll commonly see people refer to specs as tests and vice versa. The names are usually interchangeable. The main difference (arguably) is that specifications are tied to expected program behaviour. Tests are more general.

---

## Activity 2

- [ ] **NB:** don't write any source code yet
- [ ] *Again, do not implement the `count_even_numbers()` function yet!* This will be the **last** thing you do.
- [ ] create a directory to hold your **specs**. Conventionally you'll see this called `tests` in Python projects.
- [ ] in this directory create a file called `test_count_even_numbers.py`
- [ ] at the top of this file require your module that contains your test framework logic and store the export in an appropriately named variable.
- [ ] in this file write a **spec** for each of the three acceptance criteria, organising each test into the three stages of **Setup**, **Execute**, and **Verify**
- [ ] Add descriptive names for each test based on the acceptance criteria, and log the names to the console.

---

## Codify Expected Behaviour

You should have something like the below:

```python
# testing_framework.py
assert_equals = (val1, val2) => val1 === val2;
```

and a file that has the code you want to test:

```python
# test/test_count_even_numbers.py
from testing_framework import assert_equals

# --------------------------------------------------
print("Testing that [1,2,3,4,5,6] => 3")
# 1. Arrange
input = [1,2,3,4,5,6]
expected_output = 3

# 2. Act
actual_output = count_even_numbers(input)

# 3. Assert
result = assert_equals(actual_output, expected_output)
print(result)

# plus the other two tests in a similar format
```

Currently in order to run this spec, you have to run the file using `python`:

```sh
cd /path/to/project/root
python -m tests.test_count_even_numbers # you may need to use python3 or another alias for python dependent on your system
```

**Try** it yourself - this should throw an error because we **haven't written any source code** yet.

```sh
NameError: name 'count_even_numbers' is not defined
```

---
**NB:** Make sure you're seeing this error before continuing.

---

This will get tedious quickly the more spec files we add, so test frameworks have a file that runs all the specs - a *spec runner*.

---

### Spec Runners

Spec runners need 3 things you might imagine: **test framework**, **test code**, and **source code**. Usually you'll require the source code files in each spec you write - the examples in the directory use this approach.

---

## Activity 3

- [ ] In your project directory **create a file** that we'll use to run our specs called `run_tests.py`.
- [ ] In this file `import` the `os` module and the `sys` module.
- [ ] Add the src and tests directories to the Python path
  
```python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests')))
```

- [ ] Import and run the test module you created in the previous step

```python
import test_count_even_numbers
```

- [ ] Add some code to the end of `test_count_even_numbers.py` to ensure it only runs when the module is executed as a script

```python

if __name__ == "__main__":
    test_count_even_numbers()
```

- [ ] Run the `run_tests.py` file
  
---

## Further Work

Write **methods** and use **callbacks** to clean up your code!

There are lots of way to extend this framework. The options below are only possibilities - if you have ideas go explore them. Extend it as much as you want - add useful failure messages, colour output!

Discuss and share them with your coach and cohort!

How might you get this to work?

```python
test.it("returns 3", function() {
# 1. Setup
  input = [1,2,3,4,5,6];
  expected_output = 3;

# 2. Execute
  actual_output = count_even_numbers(input);

# 3. Verify
  return test.assert_equals(actual_output, expected_output);
})
```

How might you get this to work? How lovely and readable is this?!

```python
test.it("returns 3", function() {
# Setup, Execute, Verify
  test.expect(count_even_numbers([1,2,3,4,5,6])).to_wqual(3);
})
```

---

## Even further work

- How can you move your test helper code into its own repo?
- How can you allow your next project to access your test library repo?
- How can you write tests for your test library? (!)
- What API should your test library have?
- How will you publish your library? NPM?

---

## Testing and Test Frameworks - Conclusions

- **Testing** is a crucial part of software development. It helps ensure that the code works as expected and catches bugs early in the development process.
- **Unit tests** are tests that focus on individual units of code, such as functions or classes. They help ensure that each unit of code works correctly in isolation.
- **Test frameworks** provide a structured way to write and run tests. They often include assertion libraries that help compare expected and actual results.
- **Acceptance criteria** define the success criteria for a feature or piece of code. They help guide the development process and ensure that the code meets the desired requirements.
- **Edge and corner cases** are important to consider when writing tests. They help ensure that the code works correctly in all scenarios, including boundary cases.

---

<details>

## Possible Test Framework Solution

***Step 1***: Create a Simple Testing Framework
Create a file named testing_framework.py:

```python
class Expectation:
    def __init__(self, actual):
        self.actual = actual

    def to_equal(self, expected):
        assert self.actual == expected, f"Expected {expected}, but got {self.actual}"

class TestFramework:
    def it(self, description, test_func):
        try:
            test_func()
            print(f"✔ {description}")
        except AssertionError as e:
            print(f"✘ {description}")
            print(f"  {e}")

    def assert_equals(self, actual, expected):
        assert actual == expected, f"Expected {expected}, but got {actual}"

    def expect(self, actual):
        return Expectation(actual)

test = TestFramework()
```

***Step 2***: Use the Testing Framework
Create a test file named test_count_even_numbers.py:

```python
from testing_framework import test

def count_even_numbers(arr):
    return len([x for x in arr if x % 2 == 0])

test.it("returns 3", lambda: (
    # Setup, Execute, Verify
    test.expect(count_even_numbers([1, 2, 3, 4, 5, 6])).to_equal(3)
))
```

Running the Test
To run the test, simply execute the test_count_even_numbers.py script:

```sh
python test_count_even_numbers.py
```

</details>
