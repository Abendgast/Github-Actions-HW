import myapp.app

def test_add():
    assert myapp.app.add(1, 2) == 3

def test_subtract():
    assert myapp.app.subtract(3, 2) == 1
