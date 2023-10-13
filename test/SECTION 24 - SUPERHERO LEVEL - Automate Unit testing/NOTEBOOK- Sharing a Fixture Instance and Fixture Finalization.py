Sharing
a
fixture

# conftest.py

import pandas
import pytest
import math
from unittest import mock


# Defining the function with 3 parameters
@pytest.fixture(scope="module")
def xyfunc():
    # Loading the Excel (D:\\testing\\values.xlsx) values into a Pandas DataFrame
    df = pandas.read_excel("D:\\testing\\values.xlsx")

    # The value of x
    x = float(df["Price"][0])

    # The value of y
    with mock.patch('builtins.input', return_value=10):
        y = float(input("Enter the value of y: "))

    return math.pow(x / y, 2)


Now, the
test
file:


# test_results.py

def test_result1(xyfunc):
    result = round(xyfunc)
    print(id(xyfunc))
    assert result == 894
    assert 0


def test_result2(xyfunc):
    result = round(xyfunc, 1)
    print(id(xyfunc))
    assert result == 894.0
    assert 0


def test_result3(xyfunc):
    result = round(xyfunc, 2)
    print(id(xyfunc))
    assert result == 894.01
    assert 0


Running
the
tests:

D:\fixture_sharing\tests > pytest - -disable - warning
test_results.py

Fixture
finalization

# Method 1 - using the yield statement

# conftest.py

import pandas
import pytest
import math
from unittest import mock


# Defining the function with 3 parameters
@pytest.fixture(scope="module")
def xyfunc():
    # Loading the Excel (D:\\testing\\values.xlsx) values into a Pandas DataFrame
    df = pandas.read_excel("D:\\testing\\values.xlsx")

    # The value of x
    x = float(df["Price"][0])

    # The value of y
    with mock.patch('builtins.input', return_value=10):
        y = float(input("Enter the value of y: "))

    yield math.pow(x / y, 2)
    # teardown code
    print("Testing has finished!!!")
    # here you can also close any open connections/sessions/files etc.

or:

# Method 2 - using finalizers

# conftest.py

import pandas
import pytest
import math
from unittest import mock


# Defining the function with 3 parameters
@pytest.fixture(scope="module")
def xyfunc(request):
    # Loading the Excel (D:\\testing\\values.xlsx) values into a Pandas DataFrame
    df = pandas.read_excel("D:\\testing\\values.xlsx")

    # The value of x
    x = float(df["Price"][0])

    # The value of y
    with mock.patch('builtins.input', return_value=10):
        y = float(input("Enter the value of y: "))

    # teardown code
    def fin():
        print("Testing has finished!!!")
        # here you can also close any open connections/sessions/files etc.

    request.addfinalizer(fin)
    # end of teardown code

    return math.pow(x / y, 2)


### Run the test_results.py file using:

### pytest - s - -disable - warning test_results.py