"""Finding max sum of all subarray with size k"""


def max_sum_subarray(input_array, k):
    i = 0
    j = 0
    max_sum = 0
    total_sum = 0
    n = len(input_array)
    while j < n:
        total_sum += input_array[j]

        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            print(input_array[i:j+1])
            max_sum = max(max_sum, total_sum)
            total_sum -= input_array[i]
            j += 1
            i += 1

    return max_sum


if __name__ == '__main__':
    array = [2, 3, 1, 10, 10, 1, 8, 7]
    k = 4
    print(max_sum_subarray(array, k))
