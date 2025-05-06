from plates import is_valid

def test_one():
    assert is_valid('H') == False
    assert is_valid('GOODBYE') == False

def test_twp():
    assert is_valid('CS 50') == False
    assert is_valid('H.O.H') == False

def test_three():
    assert is_valid('88TT') == False
    assert is_valid('C50') == False
    assert is_valid('8TT') == False

def test_for():
    assert is_valid('CS50') == True
    assert is_valid('CS50P') == False
    assert is_valid('CS05') == False
