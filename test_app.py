import app

def test_add():
    assert app.add(3, 5) == 8
    assert app.add(0, 0) == 0
    assert app.add(-1, 1) == 0
