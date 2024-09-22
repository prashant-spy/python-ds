"""Find first and last accordance in an array with BS"""


def binary_search(input_array, target, n, search_first):
    left = 0
    right = n - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if target == input_array[mid]:
            result = mid

            if search_first:
                right = mid - 1
            else:
                left = mid + 1

        elif target < input_array[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return result


def get_first_last_occurrence(array, k):
    n = len(array)
    first = binary_search(array, k, n, True)
    if first == -1:
        return -1, -1
    last = binary_search(array, k, n, False)
    return first, last


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    k = 8
    print(get_first_last_occurrence(nums, k))
