# variable sliding window

def smallest_subarray_sum_k(input_array, k):
    n = len(input_array)
    i = 0
    j = 0
    min_len = float('inf')
    curr_sum = 0
    while j < n:
        curr_sum += input_array[j]
        while curr_sum >= k:
            min_len = min(min_len, j - i + 1)
            curr_sum -= input_array[i]
            i += 1
        j += 1
    return min_len if min_len != float('inf') else 0


if __name__ == '__main__':
    array = [2,3,1,2,4,3]
    k = 7
    # array = [1, 2]
    # k = 4

    print(smallest_subarray_sum_k(array, k))
