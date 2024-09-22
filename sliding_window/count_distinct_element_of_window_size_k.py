def count_distinct_element_of_window_size(input_array, k):
    n = len(input_array)
    i = 0
    j = 0
    mapp = {}
    ans = []
    while j < n:
        mapp[input_array[j]] = mapp.get(input_array[j], 0) + 1

        if j - i + 1 == k:
            ans.append(len(mapp))
            mapp[input_array[i]] = mapp.get(input_array[i], 0) - 1
            if mapp.get(input_array[i]) == 0:
                del mapp[input_array[i]]
            i += 1
        j += 1

    return ans


if __name__ == '__main__':
    array = [1, 2, 2, 1, 3, 1, 1, 3]
    k = 4
    print(count_distinct_element_of_window_size(array, k))
