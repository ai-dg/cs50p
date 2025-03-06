from twttr import shorten


def test_shorten():
    assert shorten("okok") == "kk"
    assert shorten("Hello world") == "Hll wrld"
    assert shorten("Test") == "Tst"
    assert shorten("Viva la vida") == "Vv l vd"
    assert shorten("OK OK OK") == "K K K"
    assert shorten("1231244") == "1231244"
    assert shorten("Bonjour a tout le monde !") == "Bnjr  tt l mnd !"
