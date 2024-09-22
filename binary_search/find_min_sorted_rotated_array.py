import sys


def find_min_sorted_rotated_array(array):
    N = len(array)
    left = 0
    high = N - 1
    ans = float('inf')

    while left <= high:
        mid = (left + high) // 2

        # edge case search space is sorted then first element is smallest
        if array[left] <= array[high]:
            ans = min(ans, array[left])
            break

        if array[left] <= array[mid]:
            ans = min(ans, array[left])
            left = mid + 1
        else:
            ans = min(ans, array[mid])
            high = mid - 1
    return ans


if __name__ == '__main__':
    array = [3, 4, 5, 1, 2]
    print(find_min_sorted_rotated_array(array))
