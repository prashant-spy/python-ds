from collections import defaultdict


def length_of_longest_k_frequency(input_array, k):
    n = len(input_array)
    i = 0
    j = 0
    max_len = 0
    mapp = defaultdict(int)

    while j < n:
        mapp[input_array[j]] = mapp.get(input_array[j], 0) + 1

        if all(freq <= k for freq in mapp.values()):
            print(input_array[i:j + 1])
            max_len = max(max_len, j - i + 1)

        elif any(freq > k for freq in mapp.values()):
            while any(freq > k for freq in mapp.values()):
                mapp[input_array[i]] -= 1
                if mapp[input_array[i]] == 0:
                    del mapp[input_array[i]]
                i += 1
        j += 1

    return max_len


if __name__ == '__main__':
    nums = [1, 2, 3, 1, 2, 3, 1, 2]
    k = 2
    print(length_of_longest_k_frequency(nums, k))
