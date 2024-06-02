def selection(array):
    n = len(array)
    for i in range(n - 1):
        i_min = i
        for j in range(i + 1, n):
            if array[j] < array[i_min]:
                i_min = j
        value = array.pop(i_min)
        array.insert(i, value)
