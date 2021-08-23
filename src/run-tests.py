#!/usr/bin/env python3


import doctest
import os
import sys

sys.path.append(os.getcwd())

CURRENT_TESTS = [
    "chapter1-base-tests.md",
    "chapter1-exercise-http-1-1-tests.md",
    "chapter1-exercise-file-urls-tests.md",
    "chapter1-exercise-redirects-tests.md",
    "chapter1-exercise-caching-tests.md",
]

    

def run_doctests(files):
    mapped_results = dict()
    for fname in files:
        mapped_results[fname] = doctest.testfile(fname)[0]
    return mapped_results

def main(argv):
    mapped_results = run_doctests(CURRENT_TESTS)
    total_state = "all passed"
    print("\nSummarised results\n")
    for name,failure_count in mapped_results.items():
        state = "passed"
        if failure_count != 0:
            state = "failed"
            total_state = "failed"
        print("{:>40}: {}".format(name, state))
    print("-"*52)
    print("{:>40}: {}".format("Final", total_state))

    return int(total_state == "failed")


if __name__ == "__main__":
    retcode = 130  # meaning "Script terminated by Control-C"

    try:
        retcode = main(sys.argv)
    except KeyboardInterrupt:
        print("")
        print("Goodbye")

    sys.exit(retcode)
