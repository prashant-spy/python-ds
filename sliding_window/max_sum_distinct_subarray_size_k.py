"""Finding maximum sum of all distinct subarray with size k"""


def max_sum_subarray(input_array, k):
    i = 0
    j = 0
    max_sum = 0
    total_sum = 0
    n = len(input_array)
    num_set = set()

    while j < n:
        if input_array[j] in num_set:
            while input_array[j] in num_set:
                num_set.remove(input_array[i])
                total_sum -= input_array[i]
                i += 1
        num_set.add(input_array[j])
        total_sum += input_array[j]

        if j - i + 1 == k:
            print(list(set(input_array[0:j + 1])))
            max_sum = max(max_sum, total_sum)
            num_set.remove(input_array[i])
            total_sum -= input_array[i]
            i += 1
        j += 1

    return max_sum if max_sum > 0 else 0


if __name__ == '__main__':
    # array = [2, 3, 1, 10, 10, 1, 8, 7]
    # array = [1, 5, 4, 2, 9, 9, 9]
    array = [5, 3, 3, 1, 1]
    k = 3
    print(max_sum_subarray(array, k))
