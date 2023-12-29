import pandas
import pytest
import math
from unittest import mock

#Defining the function with 3 parameters
@pytest.fixture(scope = "module")
def xyfunc():
    #Loading the Excel (D:\\testing\\values.xlsx) values into a Pandas DataFrame
    df = pandas.read_excel("D:\\testing\\values.xlsx")
    
    #The value of x
    x = float(df["Price"][0])
    
    #The value of y
    with mock.patch('builtins.input', return_value = 10):
        y = float(input("Enter the value of y: "))

    yield math.pow(x / y, 2)
    #teardown code
    print("Testing has finished!!!")
    #here you can also close any open connections/sessions/files etc.

#or, using finalizers:
'''
import pandas
import pytest
import math
from unittest import mock

#Defining the function with 3 parameters
@pytest.fixture(scope = "module")
def xyfunc(request):
    #Loading the Excel (D:\\testing\\values.xlsx) values into a Pandas DataFrame
    df = pandas.read_excel("D:\\testing\\values.xlsx")
    
    #The value of x
    x = float(df["Price"][0])
    
    #The value of y
    with mock.patch('builtins.input', return_value = 10):
        y = float(input("Enter the value of y: "))

    #teardown code
    def fin():
        print("Testing has finished!!!")
        #here you can also close any open connections/sessions/files etc.
    
    request.addfinalizer(fin)
    #end of teardown code
    
    return math.pow(x / y, 2)
'''