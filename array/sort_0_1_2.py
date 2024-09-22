def sort_0_1_2(arr):
    n = len(arr)
    mid = 0
    left = 0
    right = n - 1

    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 2:
            nums[right], nums[mid] = nums[mid], nums[right]
            right -= 1
        else:
            mid += 1
    return arr


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    print(sort_0_1_2(nums))
