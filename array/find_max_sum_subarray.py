# Kadane's algorithms for max sum subarray
def find_max_sum_subarray(nums):
    n = len(nums)
    current_sum = float("-inf")
    max_sum = nums[0]
    for i in range(n):
        current_sum += nums[i]
        current_sum = max(current_sum, nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == '__main__':
    nums = [-8, -3, -6, -2, -5, -4]
    print(find_max_sum_subarray(nums))
