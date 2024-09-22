# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/

def maximum_subarray_sum(nums, k):

    n = len(nums)
    i = 0
    j = 0
    max_sum = 0
    total_sum = 0
    num_set = set()
    if n < k:
        return 0

    while j < n:
        while nums[j] in num_set:
            num_set.remove(nums[i])
            total_sum -= nums[i]
            i += 1

        num_set.add(nums[j])
        total_sum += nums[j]

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            max_sum = max(max_sum, total_sum)
            num_set.remove(nums[i])
            total_sum -= nums[i]
            i += 1
            j += 1

    return max_sum if max_sum > 0 else 0


if __name__ == '__main__':
    array = [1, 5, 4, 2, 9, 9, 9]
    length = 3
    print(maximum_subarray_sum(array, length))
