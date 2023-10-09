import pytest


# Function to be tested
def my_func(x, y, z):
    return x + y + z


# Function to be tested
def my_exception():
    div = 10 / 0
    return div


# Grouping tests inside a class prefixed with 'Test'; the functions should also be prefixed with 'test'
class TestClass(object):
    def test_result1(self):
        assert my_func(1, 2, 3) == 5

    def test_result2(self):
        assert my_func(1, 2, 3) == 6


def test_result3(self):
    with pytest.raises(ZeroDivisionError):
        my_exception()


# Stop testing after the first failure
pytest - x

# Stop testing after the first N failures
pytest - -maxfail = 5

# Test discovery summary:

# 1. By default, the collection of tests starts from testpaths (if configured - list of directories in which to search for tests when pytest is run from rootdir) or from the current directory. This is a recursive search - includes sub-directories.
# 2. In these directory(-ies) it looks for test_*.py and *_test.py files.
# 3. Inside these files it looks for functions prefixed with 'test' outside of a class, or functions prefixed with 'test' inside of a class prefixed with 'Test'

# Check out the test discovery rules here: https://docs.pytest.org/en/latest/goodpractices.html#test-discovery