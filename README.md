# Tests for CS 4962 exercises

These tests will automatically be used by the github Action script 
    created for each student.
The markdown files in this repository contain the tests for each chapter's
    working state as well as tests for the assigned exercises.
It may be useful to read through the test file for each chapter before 
    implementing the web browser.
Note that this repository will be updated throughout the semester to 
   contain tests for each chapter.

## Running the tests

To run the tests on your own simply run the __src/run-tests.py__ file from the
    root directory of your web browser git.
The script will pick up the __browser.py__ file from the directory in
    which it is ran.
With no arguments this script will test the coming week's homework, but optionally an 
    argument is used to specify a chapter's tests to run such as __chapter1__ to specify
    the tests for the first chapter or __all__ to specify all tests available.
The output of the script is [doctest](https://docs.python.org/3/library/doctest.html) 
    output for each markdown file for the current chapter followed by a 
    summary of which files contain failed tests.

### Example output
    Summarised results

                      chapter1-base-tests.md: passed
         chapter1-exercise-http-1-1-tests.md: passed
        chapter1-exercise-file-urls-tests.md: passed
        chapter1-exercise-redirects-tests.md: passed
          chapter1-exercise-caching-tests.md: passed
    ----------------------------------------------------
                                   Final: all passed

## Mocked modules and methods

To facilitate testing, certain methods in standard modules have been overwritten
 in the testing framework.
These are the methods which have been mocked.
Using methods in these classes which have not been mocked may lead to incompatability
  with this test harness.
 
From the `socket`:
- `connect`
- `send`
- `makefile`
- `close`

From `ssl`:
- `wrap_socket`

