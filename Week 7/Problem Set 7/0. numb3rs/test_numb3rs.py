from numb3rs import validate


def test_first():
    assert validate("-1.0.0.0") == False
    assert validate("256.0.0.0") == False
    assert validate("a.0.0.0") == False


def test_second():
    assert validate("0.-1.0.0") == False
    assert validate("0.256.0.0") == False
    assert validate("0.a.0.0") == False


def test_third():
    assert validate("0.0.-1.0") == False
    assert validate("0.0.256.0") == False
    assert validate("0.0.a.0") == False


def test_fourth():
    assert validate("0.0.0.-1") == False
    assert validate("0.0.0.256") == False
    assert validate("0.0.0.a") == False


def test_general():
    assert validate("0.0.0.0") == True
    assert validate("0.0.0.0.0") == False
    assert validate("-1.0.0.0") == False
    assert validate("126.23.2.1") == True
