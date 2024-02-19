from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Chenchu") == "hello, Chenchu"


# To run tests from test directory we need to create another file called __init__.py on test directory itself 