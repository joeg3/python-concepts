import calc

print ("Starting test")

def test_add():
    assert calc.add(1,1) == 2

def test_literals():
    x = 3
    y = 3
    assert x == y

print ("Ending test")