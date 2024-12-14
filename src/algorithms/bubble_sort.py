def bubble(array: list) -> list:
    """Sort a list using bubble sort.

    Args:
        array (list): unsorted list

    Returns:
        list: sorted list
    """
    n: int = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
