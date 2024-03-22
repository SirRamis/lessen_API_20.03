from tools import Calculator
import pytest

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    result = calc.add(4,5)
    assert result == 9
    print(result)

def test_first():
    print("perviy test")
    result = 2+2

    assert result == 4

def test_second():
    print("vtoroy test")
    result = 2+5

    assert result == 7