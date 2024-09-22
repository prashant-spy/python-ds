def third_largest_element(nums):
    """Find second most element in array"""
    N = len(nums)

    if N < 3:
        return max(nums)

    largest = nums[0]
    for i in range(N):
        if nums[i] > largest:
            largest = nums[i]

    second_largest = third_largest = float("-inf")

    for i in range(N):
        if nums[i] > second_largest and nums[i] != largest:
            third_largest = second_largest
            second_largest = nums[i]
        elif third_largest < nums[i] < second_largest:
            third_largest = nums[i]

    return third_largest if third_largest != float('-inf') else largest


if __name__ == '__main__':
    array = [3, 2, 1]
    print(third_largest_element(array))
