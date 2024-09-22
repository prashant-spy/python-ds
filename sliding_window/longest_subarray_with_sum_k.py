# variable sliding window
def longest_subarray_sum_k(input_array, k):
    n = len(input_array)
    i = 0
    j = 0
    max_len = 0
    curr_sum = 0

    while j < n:
        curr_sum += input_array[j]
        if curr_sum == k:
            print(input_array[i:j + 1])
            max_len = max(max_len, j - i + 1)

        elif curr_sum > k:
            while curr_sum > k:
                curr_sum -= input_array[i]
                i += 1
        j += 1
    return max_len


if __name__ == '__main__':
    array = [1,1,1]
    k = 2
    print(longest_subarray_sum_k(array, k))
