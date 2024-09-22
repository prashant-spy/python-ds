def print_subsequence_with_sum_k(index, temp_array, s, k, input_array, n):
    if index >= n:
        if s == k:
            print(temp_array)
        return

    temp_array.append(input_array[index])
    s += input_array[index]
    print_subsequence_with_sum_k(index + 1, temp_array, s, k, input_array, n)

    s -= input_array[index]
    temp_array.pop()
    print_subsequence_with_sum_k(index + 1, temp_array, s, k, input_array, n)


if __name__ == '__main__':
    input_array = [1, 2, 1]
    n = len(input_array)
    k = 2
    temp_array = []
    print(print_subsequence_with_sum_k(0, temp_array, 0, k, input_array, n))
