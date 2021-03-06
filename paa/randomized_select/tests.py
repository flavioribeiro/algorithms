from randomized_select import *

def test_select_minimum():
    data = [1, 7, 3, 5, 0, 9, 4, 6, 2, 8]
    assert 0 == RANDOMIZED_SELECT(data, 0, len(data), 0)

def test_select_maximum():
    data = [1, 7, 3, 5, 0, 9, 4, 6, 2, 8]
    assert 9 == RANDOMIZED_SELECT(data, 0, len(data), 9)

def test_select_median():
    data = [1, 7, 3, 5, 0, 9, 4, 6, 2, 8]
    assert 4 == RANDOMIZED_SELECT(data, 0, len(data), 4)
    assert 5 == RANDOMIZED_SELECT(data, 0, len(data), 5)

def test_select_terceiro_menor():
    data = [20, 10, 12, 30, 16, 100, 70]

    assert 30 == RANDOMIZED_SELECT(data, 0, len(data), 4)
    assert 10 == RANDOMIZED_SELECT(data, 0, len(data), 0)
    assert 16 == RANDOMIZED_SELECT(data, 0, len(data), 2)
