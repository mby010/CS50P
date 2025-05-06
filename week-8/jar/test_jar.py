from jar import Jar
import pytest

def test__init():
    jar = Jar(2)
    assert jar.capacity == 2


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(12)
    jar.deposit(8)
    assert jar.size == 8
    with pytest.raises(ValueError):
         jar.deposit(14)


def test_withdraw():
    jar = Jar(12)
    jar.deposit(12)
    jar.withdraw(5)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar.withdraw(10)
