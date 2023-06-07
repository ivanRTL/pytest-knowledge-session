from src.functions import add_one

def test_add_one_pass():
    assert add_one(5) == 6

def test_add_one_fail():
    assert add_one(5) == 5