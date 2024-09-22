def find_peak_element(input_array):
    n = len(input_array)
    if n == 1:
        return 0
    if input_array[0] > input_array[1]:
        return 0
    if input_array[n - 1] > input_array[n - 2]:
        return n - 1

    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2
        # if array[mid] is peak
        if input_array[mid] > input_array[mid - 1] and input_array[mid] > input_array[mid + 1]:
            return mid
        # if arr[mid] is in left side
        elif input_array[mid] > input_array[mid - 1]:
            low = mid + 1
        # if arr[mid] is in right side
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    array = [1, 3, 8, 12, 4, 2]
    out = find_peak_element(array)
    print(array[out])
