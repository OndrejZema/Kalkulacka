import sys
sys.path.append("../")

from app import calculate, is_number
import pytest

@pytest.mark.parametrize("text", ("222", "222.222"))
def test_is_number(text):
    number = is_number(text)
    assert(number)

@pytest.mark.parametrize("text", ("222,", ".222.222", "2222,222", "aaa"))
def test_is_not_number(text):
    number = is_number(text)
    assert(not number)

@pytest.mark.parametrize(["num1", "num2", "opr"], [(2, 3, "+")])
def test_add(num1, num2, opr):
    number = calculate(num1, num2, opr)
    assert(number == 5)
@pytest.mark.parametrize(["num1", "num2", "opr"], [(2, 3, "-")])
def test_sub(num1, num2, opr):
    number = calculate(num1, num2, opr)
    assert(number == -1)

@pytest.mark.parametrize(["num1", "num2", "opr"], [(2, 3, "*")])
def test_mul(num1, num2, opr):
    number = calculate(num1, num2, opr)
    assert(number == 6)

@pytest.mark.parametrize(["num1", "num2", "opr"], [(6, 3, "/")])
def test_div(num1, num2, opr):
    number = calculate(num1, num2, opr)
    assert(number == 2)

@pytest.mark.parametrize(["num1", "num2", "opr"], [(2, 0, "/")])
def test_div_zero(num1, num2, opr):
    number = calculate(num1, num2, opr)
    assert(number == None)