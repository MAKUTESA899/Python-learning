import addition


def test_add():
    assert addition.add(1, 3) == 4
    assert addition.add(-1, 1) == 0
    assert addition.add(0, 0) == 0