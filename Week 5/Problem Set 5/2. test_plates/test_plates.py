from plates import is_valid


def test_starts_with_two_letters():
    assert is_valid("AB123") == True
    assert is_valid("A123") == False
    assert is_valid("123ABC") == False
    assert is_valid("A!@#") == False
    assert is_valid("ABC") == True


def test_length_of_plates():
    assert is_valid("A") == False
    assert is_valid("ADSEFTGEDW") == False


def test_numbers_in_the_middle():
    assert is_valid("AAA4") == True
    assert is_valid("AA4A") == False


def test_no_special_chars():
    assert is_valid("C  S  5 0") == False
    assert is_valid("PI3.14") == False


def test_zero_placement():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
