def subarray_k_distinct(input_str, k):
    n = len(input_str)
    i = 0
    j = 0
    count = 0
    mapp = {}

    while j < n:
        mapp[input_str[j]] = mapp.get(input_str[j], 0) + 1

        if len(mapp) > k:
            while len(mapp) > k:
                mapp[input_str[i]] -= 1
                if mapp[input_str[i]] == 0:
                    del mapp[input_str[i]]
                i += 1

        count += j - i + 1
        j += 1
    return count


def subarray_with_k_different_integer(nums, k):
    return subarray_k_distinct(nums, k) - subarray_k_distinct(nums, k - 1)


if __name__ == '__main__':
    arr = [1, 2, 1, 2, 3]
    k = 2
    print(subarray_with_k_different_integer(arr, k))
