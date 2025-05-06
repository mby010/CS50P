from numb3rs import validate

def test_one():
    assert validate('255.255.255.255') == True
    assert validate('0.0.0.0') == True

def test_two():
    assert validate('1111') == False
    assert validate('0.0.0.1256') == False
    assert validate('0.0.0.25.1') == False
    assert validate('259.0.1.2') == False
    assert validate('120.0.0.270') == False
    assert validate('cat') == False
