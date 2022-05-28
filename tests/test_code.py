from src.code import greeting, adder


def test_greeting():
    assert greeting('Joe') == "Hello Joe"

def test_adder():
    assert adder(1, 2) == 3
    assert adder(3, 4) == 8

