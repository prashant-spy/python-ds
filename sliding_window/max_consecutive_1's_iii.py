# https://leetcode.com/problems/max-consecutive-ones-iii/

def max_consecutive_one(array, k):
    n = len(array)
    i = 0
    j = 0
    count = 0
    max_len = 0

    while j < n:
        if nums[j] == 0:
            count += 1

        if count <= k:
            max_len = max(max_len, j - i + 1)

        elif count > k:
            while count > k:
                if nums[i] == 0:
                    count -= 1
                i += 1
        j += 1
    return max_len


if __name__ == '__main__':
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    print(max_consecutive_one(nums, k))
