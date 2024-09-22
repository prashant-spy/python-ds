"""https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/"""


def count_complete_subarray(array, k):
    n = len(array)
    i = 0
    j = 0

    subarray_count = 0
    mapp = {}

    while j < n:
        mapp[array[j]] = mapp.get(array[j], 0) + 1

        while len(mapp) == k:
            subarray_count += (n - j)
            mapp[array[i]] -= 1
            if mapp[array[i]] == 0:
                del mapp[array[i]]
            i += 1
        j += 1

    return subarray_count


if __name__ == '__main__':
    nums = [1, 3, 1, 2, 2]
    k = len(set(nums))
    print(count_complete_subarray(nums, k))
