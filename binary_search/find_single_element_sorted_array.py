def find_single_element_sorted_array(array):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if mid % 2 == 1:
            mid -= 1

        if nums[mid] != nums[mid + 1]:
            right = mid
        else:
            left = mid + 2
    return nums[left]


if __name__ == '__main__':
    nums = [1,1,2,2,3,5,5,6,6]
    print(find_single_element_sorted_array(nums))
