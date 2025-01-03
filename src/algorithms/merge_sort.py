def merge_sort(array: list) -> list:
    """Sort a list using merge sort.

    Args:
        array (list): unsorted list

    Returns:
        list: sorted list
    """
    if len(array) == 1:
        return array
    else:
        mid_index: int = len(array) // 2
        left_array: list = array[:mid_index]
        right_array: list = array[mid_index:]
        merge_sort(left_array)
        merge_sort(right_array)
        return _merge(array, left_array, right_array)


def _merge(array: list, left_array: list, right_array: list) -> list:
    i: int = 0
    j: int = 0
    k: int = 0

    # Compare the array elements and place in order
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    # Place any left over elements
    while i < len(left_array):
        array[k] = left_array(i)
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array(j)
        j += 1
        k += 1
