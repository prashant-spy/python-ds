def search_insert_position(input_array, target):
    n = len(input_array)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    k = 5
    print(search_insert_position(nums, k))
