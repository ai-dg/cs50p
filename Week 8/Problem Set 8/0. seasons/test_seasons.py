from seasons import *
import pytest


def test_valid_dates():
    with pytest.raises(ValueError):
        check_and_get_date("January 1, 1999")
    with pytest.raises(ValueError):
        check_and_get_date("1999-13-01")
    with pytest.raises(ValueError):
        check_and_get_date("1999-12-00")
    with pytest.raises(ValueError):
        check_and_get_date("1999-12-32")
    with pytest.raises(ValueError):
        check_and_get_date("1999-00-01")
