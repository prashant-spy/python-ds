def count_number_1(array, left=None, right=None):
    if not array:
        return 0

    if left is None and right is None:
        left = 0
        right = len(array) - 1

    if array[right] == 0:
        return 0

    if array[left] == 1:
        return right - left + 1

    mid = (left + right) // 2

    return count_number_1(array, left, mid) + count_number_1(array, mid + 1, right)


if __name__ == '__main__':
    nums = [0, 0, 0, 0, 1, 1, 1]
    print(count_number_1(nums))
