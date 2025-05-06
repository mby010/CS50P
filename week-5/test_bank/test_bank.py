from bank import value

def test_val0():
    assert value('HeLLoooo') == 0
    assert value('HELLO') == 0
    assert value('hello, friend!') == 0

def test_val1():
    assert value('Hey') == 20
    assert value('How are you?') == 20
    assert value('how you doing :)') == 20

def test_val2():
    assert value('3aslama') == 100
    assert value('Bonjour, ça va?') == 100
