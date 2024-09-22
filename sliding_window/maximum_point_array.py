def max_point_array(input_array, k):
    """collect max sum in an array using of k moves sliding window concept"""
    left_sum = 0
    right_sum = 0
    max_len = 0
    for i in range(k):
        left_sum += input_array[i]
        max_len = left_sum

    rindex = len(input_array) - 1
    for j in range(k - 1, -1, -1):
        left_sum -= input_array[j]
        right_sum += input_array[rindex]
        rindex -= 1
        max_len = max(max_len, left_sum + right_sum)

    return max_len


if __name__ == '__main__':
    array = [100, 40, 17, 9, 73, 75]
    k = 3
    print(max_point_array(array, k))
