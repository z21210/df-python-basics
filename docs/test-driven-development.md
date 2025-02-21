# Test-Driven Development

## Overview

There are many different practices and techniques used to develop software.  All have their own merits, advantages and disadvantages. Test-Driven Development is one such technique that comes from the set of Extreme Programming practices developed by Agile pioneer, Kent Beck.  This course will introduce the methodology needed for Test-Driven Development.

---

## Aims

The aim of this course is to allow you begin to explore different ways of developing and testing software so that you can appreciate the need for the thorough testing of code, the ways in which tests can be administered and how bugs can be identified and fixed.

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

## Test-Driven Development - Connections

Work in your your allotted groups to sequence the following steps into a sensible order for developing and testing code.

Arrange only the relevant tasks in TDD order (You can repeat a task):

- *Execute test*
- *Write failing test*
- *Repeat*
- *Execute Test*
- *Refactor*
- *Analyse Coverage*
- *Write just enough code to pass*
- *Debug*
- *Test performance of tests*

**Timebox:** 10 minutes

---

## Test-Driven Development - Concepts

### What is TDD?

- Core practice of XP
- Can be adopted within other methodologies

> "Test-first programming is the least controversial and most widely adopted part of Extreme Programming (XP). By now the majority of professional Java™ programmers have probably caught the testing bug" – Elliotte Rusty Harold [Who is Elliotte Rusty Harold?](https://en.wikipedia.org/wiki/Elliotte_Rusty_Harold)

- Test written before implementation
- Tools and techniques make TDD very rigorous process
- aka Test Driven Design
- Tests drive design of API
- Developers become "Test infected" (Erich Gamma - [Who is Erich Gamma?](https://en.wikipedia.org/wiki/Erich_Gamma))
  - Cannot program without test first

### The Three Rules of TDD

1. You are not allowed to write any production code unless it is to make a failing unit test pass.
2. You are not allowed to write any more of a unit test than is sufficient to fail; and compilation failures are failures.
3. You are not allowed to write any more production code than is sufficient to pass the one failing unit test.

**This is according to Uncle Bob!** [Who is Uncle Bob?](https://en.wikipedia.org/wiki/Robert_C._Martin)

### Test – Code – Refactor

Kent Beck's [Who is Kent Beck?](https://en.wikipedia.org/wiki/Kent_Beck) summary of TDD:

1. Write new code only if you first have a failing automated test
2. Eliminate duplication

#### Red - Green - Refactor

![Red-Green-Refactor-1](../images/rgrf1.png)

The image above illustrates that the famous green bar is indeed a progress bar. The image below shows the final outcome of running this series of tests: there are 3 failures.

![Red-Green-Refactor2](../images/rgrf2.png)

#### Red-Green-Refactor Workflow

![Red-Green-Refactor Workflow](../images/rgrf3.png)

---

### More on TDD

#### TDD Benefits

- Build up library of small tests that protect against regression bugs
- Extensive code coverage
- No code without a test
- No code that is not required
- Almost completely eliminates debugging
- More than offsets time spent developing tests
- Tests as developer documentation
- Confidence not fear
- Confidence in quality of the code; confidence to refactor
- A regression bug is a defect which stops some bit of functionality working, after an event such as a code release, or refactoring.

#### TDD Strategies

More from Kent Beck:

- Fake it:
  - Return a *constant*; gradually replace *constants* with *variables*
- Obvious implementation:
  - If a quick, clean solution is obvious, type it in
- Triangulation:
  - Locating a transmitter by taking bearings from 2 or more receiving stations
  - Only generalise code when you have 2 or more different tests

The point is to get developers to work in very small steps, continually re-running the tests.

```sh
                   <=> A
                  /  \
                 /    \
                /      \
               /        \
              /          \
             /            \
            ¶              []
            B               C
```

**Triangulation:** someone on the boat at A can determine their position on a chart by taking compass bearings to the lighthouse at B and the tower at C. Or conversely, observers at B and C can work out the location of the boat by taking bearings to it from their known points on the shore and sharing their readings. In fact, sailors are taught to take a three-point fix, with charted landmarks that are as widely separated as possible, for better accuracy.

#### Testing Heuristics

**Test List:**

- Start by writing a list of all tests you know you have to write

**Starter Test:**

- Start with case where output should be same as input

**One Step Test:**

- Start with test that will teach you something and you are confident you can implement

**Explanation Test:**

- Ask for and give explanations in terms of tests

**Learning Tests:**

- Check your understanding of a new API by writing tests

These mainly come from Kent Beck's book **Test Driven Development**, *Chapter 26 – "Red Bar Patterns"*. They're primarily suggestions for breaking down a seemingly mountainous task of developing some new functionality in a test-driven way, into very small, tractable steps.

For example:

> "a poster on the Extreme Programming newsgroup asked about how to write a polygon reducer test-first.
>
> The input is a mesh of polygons and the output is a mesh of polygons that describes precisely the same surface, but with the fewest possible polygons.
>
> How can I test-drive this problem since getting a test to work requires reading Ph.D. theses?”
>
> **Starter Test** provides an answer:
>
> The output should be the same as the input.
>
> Some configurations of polygons are already normalized, incapable of further reduction. The input should be as small as possible, like a single polygon, or even an empty list of polygons."
>
> **Explanation Test** is primarily for communicating within the development group, clarifying the requirements for some item of functionality by expressing them precisely in terms of tests.

---

## Test-Driven Development - Concrete Practice

## Activity 1

Test-drive the sister function for the *Count-even numbers function*: count **odd** numbers.

Write a program that you can run that can find how many **odd** numbers are in a list of numbers.

Remember the 3 rules of TDD!

### Activity 1 - Acceptance Criteria

```sh
Input => Output
[1,2,3,4,5,6] => 3
[0,1,2] => 1
[2,4,6] => 0
```

---

## Activity 2

Test-drive a function that can find the **average** of a list of numbers.

Write a program that you can run that can find the average of a list of numbers.

Remember the 3 rules of TDD!

### Activity 2 - Acceptance Criteria

```sh
Input => Output
[1,2,3,4,5,6] => 3.5
[0,1,2] => 1
[2,4,6] => 4
```

---

## Activity 3

Given a word, compute the scrabble score for that word.

### Letter Values

You'll need these:

| Letter                       | Value |
| ---------------------------- | ----- |
| A, E, I, O, U, L, N, R, S, T | 1     |
| D, G                         | 2     |
| B, C, M, P                   | 3     |
| F, H, V, W, Y                | 4     |
| K                            | 5     |
| J, X                         | 8     |
| Q, Z                         | 10    |

Example
"cabbage" should be scored as worth 14 points:

- 3 points for C
- 1 point for A, twice
- 3 points for B, twice
- 2 points for G
- 1 point for E

And to total:

```text
3 + 2x1 + 2x3 + 2 + 1
= 3 + 2 + 6 + 3
= 14
```

## Acceptance Criteria

```python
scrabble = Scrabble('')
print(scrabble.score())  # => 0

scrabble = Scrabble(" \t\n")
print(scrabble.score())  # => 0

scrabble = Scrabble(None)
print(scrabble.score())  # => 0

scrabble = Scrabble('a')
print(scrabble.score())  # => 1

scrabble = Scrabble('f')
print(scrabble.score())  # => 4

scrabble = Scrabble('street')
print(scrabble.score())  # => 6

scrabble = Scrabble('quirky')
print(scrabble.score())  # => 22

scrabble = Scrabble('OXYPHENBUTAZONE')
print(scrabble.score())  # => 41
```

- `Scrabble` should be a `class` that you add methods (functions) to (e.g. `score`)

## Extended Acceptance Criteria - just for fun - no tests exist for these

> Each `Scrabble` method should be no more than 5 lines and contain no more than 5 operations.
> You can play a double or a triple letter.
> You can play a double or a triple word.

- Can you write tests for these based on the the test structure above?
- Can you test drive these functions?

---

## Test-Driven Development - Conclusions

- **TDD** is part of the Agile methodology, stemming from Extreme Programming
- **TDD** is often implemented as part of Pair Programming
- **TDD** makes developers think about the functionality of the code before writing it
- There are **3 rules** that are generally followed when implementing **TDD**
  - Write a failing test
  - Write the code to pass the test
  - Refactor the code

---

## Bob's Bagels - An Exercise in TDD

You have already done some Domain Modelling for Bob's Bagels, so now, you and your Pair Programmer can attempt to Test Drive the development of the code!

A good pair programming technique to use here would be ***Ping Pong***:

Like a game of Table Tennis:

- One writes a test and bats it over the the other
- The other writes the code for the test and then writes a new test that is batted back to the partner
- Ad infinitum until all of the code has been written!

[Bob's Bagels](../activities/bobs-bagels/bobs-bagels.md)

---
