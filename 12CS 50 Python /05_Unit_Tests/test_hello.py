from hello import hello 

def test_default():
    assert hello() == "hello, world"

def test_arguments():
    assert hello("Chenchu") == "hello, Chenchu"

def test_using_Loop():
    for name in ["ram", "bheem", "ravan", "arjun", "palgun"]:
        assert hello(name) == f"hello, {name}"

#should run it as pytest test_hello.py