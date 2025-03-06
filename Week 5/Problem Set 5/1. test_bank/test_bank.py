from bank import value


def test_hello():
    assert value("Hello") == 0
    assert value("Hello there") == 0


def test_h():
    assert value("How are you") == 20
    assert value("How are you doing?") == 20


def test_other():
    assert value("See you") == 100
    assert value("What's up!") == 100
