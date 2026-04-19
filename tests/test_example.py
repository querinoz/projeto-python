import pytest
import sys;sys.path.append('.')
from app import add_numbers

def test_add_positive():
    assert add_numbers(1, 2) == 2

def test_add_zero():
    assert add_numbers(1, 0) == 0

def test_add_negative():
    assert add_numbers(4, -100) == -400

def test_add_string__expect_exception():
    with pytest.raises(TypeError):
        add_numbers("a", "b")
