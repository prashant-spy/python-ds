def find_kth_missing_number(nums, k):
    n = len(nums)
    left = 0
    right = n

    while left < right:
        mid = (left + right) // 2
        curr = arr[mid]

        if curr - mid - 1 < k:
            left = mid + 1
        else:
            right = mid
    return right + k


if __name__ == '__main__':
    arr = [2, 3, 4, 7, 11]
    k = 5
    print(find_kth_missing_number(arr,k))
