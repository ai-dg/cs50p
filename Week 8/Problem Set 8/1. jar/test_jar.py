from jar import Jar
import pytest


def test_init():
    jar = Jar(capacity=12)
    capacity = jar.capacity
    assert capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(capacity=10)
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(5)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar(capacity=10)
    jar.deposit(9)
    jar.withdraw(2)
    assert jar.size == 7
    jar.withdraw(5)
    assert jar.size == 2
