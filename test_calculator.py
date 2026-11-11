def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 10


def test_add_negative():
    assert add(-1, 1) == 0
