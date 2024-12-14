def selection(array: list) -> list:
    """Sort a list using selection sort.

    Args:
        array (list): unsorted list

    Returns:
        list: sorted list
    """
    n: int = len(array)
    for i in range(n - 1):
        i_min: int = i
        for j in range(i + 1, n):
            if array[j] < array[i_min]:
                i_min = j
        value: int = array.pop(i_min)
        array.insert(i, value)
    return array
