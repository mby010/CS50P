from twttr import shorten

def test_shorten():
    assert shorten('CS50') == 'CS50'
    assert shorten('cs50') == 'cs50'
    assert shorten('HeLlO') == 'HLl'
    assert shorten('PI = 3.14') == 'P = 3.14'
