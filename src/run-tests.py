#!/usr/bin/env python3


import argparse
import doctest
import os
import sys
import re

sys.path.append(os.getcwd())

CURRENT_TESTS = {
    "chapter1" : ["chapter1-base-tests.md",
                  "chapter1-exercise-http-1-1-tests.md",
                  "chapter1-exercise-file-urls-tests.md",
                  "chapter1-exercise-redirects-tests.md",
                  "chapter1-exercise-caching-tests.md",
                  ],
    "chapter2" : ["chapter2-base-tests.md",
                  "chapter2-exercise-line-breaks-tests.md",
                  "chapter2-exercise-resizing-tests.md",
                  "chapter2-exercise-mouse-wheel-tests.md",
                  "chapter2-exercise-zoom-tests.md",
                  ],
    "chapter3" : ["chapter3-base-tests.md",
                  "chapter3-exercise-centered-text-tests.md",
                  "chapter3-exercise-superscripts-tests.md",
                  "chapter3-exercise-soft-hyphens-tests.md",
                  "chapter3-exercise-small-caps-tests.md",
                  ],
}

all_tests = list()
specific_file_tests = {}

''' 
add option to run all tests by running script w/ argval 'all',
and add option to run individual test files by name (removing '-exercise-' infix substring if present)
'''
for tests in CURRENT_TESTS.values():
    all_tests.extend(tests)

    for test in tests:
        arg_val = re.sub(r'-exercise', '', test).removesuffix('-tests.md')
        specific_file_tests[arg_val] = [test]

CURRENT_TESTS["all"] = all_tests

CURRENT_TESTS |= specific_file_tests


def run_doctests(files):
    mapped_results = dict()
    for fname in files:
        mapped_results[fname] = doctest.testfile(fname,
                                                 optionflags=doctest.ELLIPSIS)
    return mapped_results

def parse_arguments(argv):
    parser = argparse.ArgumentParser(description='WBE test runner')
    parser.add_argument("chapter",
                        nargs="?",
                        default="chapter3",
                        choices=list(CURRENT_TESTS),
                        help="Which chapter's tests to run")
    args = parser.parse_args(argv[1:])

    return args

def main(argv):
    args = parse_arguments(argv)
    tests = CURRENT_TESTS[args.chapter]
    mapped_results = run_doctests(tests)
    total_state = "all passed"
    print("\nSummarised results\n")
    for name,(failure_count, test_count) in mapped_results.items():
        state = "passed"
        if failure_count != 0:
            state = "failed {:<2} out of {:<2} tests".format(failure_count, test_count)
            total_state = "failed"
        print("{:>40}: {}".format(name, state))
    print("-"*52)
    print("{:>40}: {} ".format("Final", total_state))

    return int(total_state == "failed")


if __name__ == "__main__":
    retcode = 130  # meaning "Script terminated by Control-C"

    try:
        retcode = main(sys.argv)
    except KeyboardInterrupt:
        print("")
        print("Goodbye")

    sys.exit(retcode)
