def binary_search(array, target, search_first):
    n = len(array)

    left = 0
    right = n - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if target == array[mid]:
            result = mid

            if search_first:
                right = mid - 1
            else:
                left = mid + 1

        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return result


if __name__ == '__main__':
    nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
    k = 6

    first = binary_search(nums, k, True)  # first occurrence of number
    last = binary_search(nums, k, False)  # last occurrence of number

    count = last - first + 1

    if first != -1:
        print(f"Element {k} occurs {count} times")
    else:
        print('Element found not in the list')
    i = 1
