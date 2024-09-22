
# fixed sliding widgets code

from collections import deque


def max_of_subarray_of_size_k(input_array, k):
    ans = []
    deq = deque()
    n = len(input_array)
    i = 0
    j = 0

    while j < n:
        while deq and input_array[j] > input_array[deq[-1]]:
            deq.pop()
        deq.append(j)

        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            ans.append(input_array[deq[0]])

            if deq[0] == i:
                deq.popleft()
            i += 1
            j += 1

    return ans


if __name__ == '__main__':
    arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    k = 4
    print(max_of_subarray_of_size_k(arr, k))  # Output should be [3, 4, 5, 5, 5, 6]
