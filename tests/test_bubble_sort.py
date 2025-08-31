from algorithms import bubble


def test_bubble_simple():
    assert bubble([]) == []
    assert bubble([0]) == [0]
    assert bubble([1]) == [1]
    assert bubble([-1]) == [-1]


def test_bubble_odd():
    odd_array: list[int] = [1, 2, 3]
    assert bubble([1, 2, 3]) == odd_array
    assert bubble([1, 3, 2]) == odd_array
    assert bubble([2, 1, 3]) == odd_array
    assert bubble([2, 3, 1]) == odd_array
    assert bubble([3, 1, 2]) == odd_array
    assert bubble([3, 2, 1]) == odd_array


def test_bubble_even():
    even_array: list[int] = [1, 2, 3, 4]
    assert bubble([1, 2, 3, 4]) == even_array
    assert bubble([4, 3, 2, 1]) == even_array


def test_bubble_negative():
    negative_array: list[int] = [-3, -2, -1]
    assert bubble([-3, -2, -1]) == negative_array
    assert bubble([-1, -2, -3]) == negative_array


def test_bubble_mixed():
    assert bubble([-1, 1]) == [-1, 1]
    assert bubble([1, -1]) == [-1, 1]
    assert bubble([-1, 0, 1]) == [-1, 0, 1]
    assert bubble([1, 0, -1]) == [-1, 0, 1]
