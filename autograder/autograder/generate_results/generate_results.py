
import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('run_tests', top_level_dir='run_tests')
    JSONTestRunner(visibility='visible').run(test_suite)
