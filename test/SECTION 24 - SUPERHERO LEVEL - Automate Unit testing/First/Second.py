import pytest

def my_exception():
    div = 10 / 0
    return div

def test_result_second():
    with pytest.raises(ZeroDivisionError):
        my_exception()