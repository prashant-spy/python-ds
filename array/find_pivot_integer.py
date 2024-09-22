def find_pivot_integer(input_array):
    n = len(input_array)
    max_sum = n * (n + 1) // 2
    for i in range(1, n + 1):
        curr_sum = i * (i + 1) // 2
        remain_sum = max_sum - curr_sum + i

        if curr_sum == remain_sum:
            return i
    return -1


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    print(find_pivot_integer(array))
