def print_all_distinct_subarray(array):
    mapp = {}

    for val in array:
        mapp[val] = False

    i = 0
    j = 0
    n = len(array)
    while j < n:
        while j < n and not mapp[array[j]]:
            mapp[array[j]] = True
            j += 1

        print(array[i:j+1])

        while j < n and mapp[array[j]]:
            mapp[array[i]] = False
            i += 1


if __name__ == '__main__':
    A = [5, 2, 3, 5, 4, 3]
    print(print_all_distinct_subarray(A))
