def print_all_subsequence(index, dummy_array, input_array, n):
    if index >= n:
        print(dummy_array)
        return

    dummy_array.append(input_array[index])
    print_all_subsequence(index + 1, dummy_array, input_array, n)
    dummy_array.pop()
    print_all_subsequence(index + 1, dummy_array, input_array, n)


if __name__ == '__main__':
    array = [3, 2, 1]
    n = len(array)
    temp_array = []
    print(print_all_subsequence(0, temp_array, array, n))
