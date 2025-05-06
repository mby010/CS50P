from working import convert
import pytest

def test_one():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:48 PM to 12:41 AM') == '21:48 to 00:41'

def test_two():
    assert convert('4:44 PM to 4 AM') == '16:44 to 04:00'
    assert convert('7 AM to 12:01 PM') == '07:00 to 12:01'

def test_three():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60')


def test_four():
    with pytest.raises(ValueError):
        convert('09:00 AM to 17:00 PM')


def test_five():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
