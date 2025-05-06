from um import count

def test_one():
    assert count('uM...') == 1
    assert count('um, um?') == 2
    assert count('HELLO, UM...FRIEND') == 1
def test_two():
    assert count('yummy') == 0
    assert count('I like this album') == 0

def test_three():
    assert count('um, hello, um, world') == 2
    assert count('Um, thanks, um...') == 2
