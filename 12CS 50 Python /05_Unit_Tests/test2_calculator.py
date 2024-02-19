from calculator import square

def test_square():
    assert square(2) == 4
    assert square(4) == 16
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

# should run this as pytest test2_calculator.py