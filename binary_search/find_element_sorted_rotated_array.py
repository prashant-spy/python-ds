def find_element_rotated_sorted_array(array, target):
    """Find element in sorted rotated unique/duplicate array
    or
    This solves searching for an element in a Bitonic Array"""

    N = len(array)
    low = 0
    high = N - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid

        # shrinking array from both side if duplicate element is present
        if array[low] == array[mid] and array[mid] == array[high]:
            low += 1
            high -= 1
            continue

        if array[low] <= array[mid]:
            # find sorted left half and eliminate
            if array[low] <= target <= array[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # find sorted right half and eliminate
            if array[mid] <= target <= array[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


if __name__ == '__main__':
    # array = [4, 5, 6, 7, 0, 1, 2]
    array = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
    target = 3
    print(find_element_rotated_sorted_array(array, target))
