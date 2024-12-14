from src.algorithms.bubble_sort import bubble


def test_bubble_simple():
    assert bubble([]) == []
    assert bubble([0]) == [0]
    assert bubble([1]) == [1]
    assert bubble([-1]) == [-1]


def test_bubble_odd():
    assert bubble([1, 2, 3]) == [1, 2, 3]
    assert bubble([1, 3, 2]) == [1, 2, 3]
    assert bubble([2, 1, 3]) == [1, 2, 3]
    assert bubble([2, 3, 1]) == [1, 2, 3]
    assert bubble([3, 1, 2]) == [1, 2, 3]
    assert bubble([3, 2, 1]) == [1, 2, 3]


def test_bubble_even():
    assert bubble([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert bubble([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_bubble_negative():
    assert bubble([-3, -2, -1]) == [-3, -2, -1]
    assert bubble([-1, -2, -3]) == [-3, -2, -1]


def test_bubble_mixed():
    assert bubble([-1, 1]) == [-1, 1]
    assert bubble([1, -1]) == [-1, 1]
    assert bubble([-1, 0, 1]) == [-1, 0, 1]
    assert bubble([1, 0, -1]) == [-1, 0, 1]
