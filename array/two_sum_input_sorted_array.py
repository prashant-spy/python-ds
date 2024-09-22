# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

def two_sum_input_sorted_array(arr, k):
    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]

        if total < k:
            left += 1
        elif total > k:
            right -= 1
        else:
            return [left + 1, right + 1]


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    print(two_sum_input_sorted_array(numbers, target))
