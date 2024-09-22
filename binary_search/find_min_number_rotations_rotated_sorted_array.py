"""Find the Rotation Count in Rotated Sorted array"""


def find_min_number_rotations(array):
    n = len(array)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[left] <= nums[right]:
            return left

        if nums[mid] <= nums[mid + 1] and nums[mid] <= nums[mid - 1]:
            return mid

        if nums[left] <= nums[mid]:
            left = mid + 1
        else:
            right = mid - 1


if __name__ == '__main__':
    nums = [8, 9, 10, 2, 5, 6]
    print(find_min_number_rotations(nums))
