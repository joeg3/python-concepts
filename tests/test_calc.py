from src import calc

def test_add():
     assert calc.add(1,1) == 2

def test_equal():
    x = 3
    y = 3
    assert x == y

def test_not_equal():
    x = 3
    y = 2
    assert x != y