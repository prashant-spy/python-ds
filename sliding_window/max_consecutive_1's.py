def length_of_max_subarray_1(array, k):
    i = 0
    j = 0
    n = len(array)
    max_len = 0
    zero = 0

    while j < n:
        if array[j] == 0:
            zero += 1

        elif zero <= k:
            max_len = max(max_len, j - i + 1)

        elif zero > k:
            if array[i] == 0:
                zero -= 1
                i += 1
        j += 1
    return max_len


if __name__ == '__main__':
    array = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    print(length_of_max_subarray_1(array, k))
