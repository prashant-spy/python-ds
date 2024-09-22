def find_unique_elements_sorted_array(arr):
    def binary_search(lo, hi):
        if lo > hi:
            return []

        mid = lo + (hi - lo) // 2

        # Check if the mid element is unique
        if (mid == 0 or arr[mid] != arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] != arr[mid + 1]):
            return [arr[mid]]

        # Left side search
        if mid % 2 == 0:
            if arr[mid] == arr[mid + 1]:
                return binary_search(mid + 2, hi)
            else:
                return binary_search(lo, mid - 1)
        else:
            if arr[mid] == arr[mid - 1]:
                return binary_search(mid + 1, hi)
            else:
                return binary_search(lo, mid - 2)

    # Apply binary search on the whole array
    n = len(arr)
    return binary_search(0, n - 1)


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 3, 4, 5, 5, 6, 6]
    print(find_unique_elements_sorted_array(nums))
