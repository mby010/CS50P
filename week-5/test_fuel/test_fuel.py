from fuel import gauge, convert
import pytest

def test_gauge():
    assert gauge(47) == '47%'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'

def test_convert():
    assert convert('1/4') == 25
    
    with pytest.raises(ValueError):
        convert('4/3')

    with pytest.raises(ZeroDivisionError):
        convert('0/0')
