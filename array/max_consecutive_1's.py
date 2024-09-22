def max_consecutive_one_count(input_array):
    count = 0
    max_count = 0

    for item in input_array:
        if item == 1:
            count += 1
        else:
            count = 0
        max_count = max(max_count, count)

    return max_count


if __name__ == '__main__':
    array = [1, 1, 0, 1, 1, 1]
    print(max_consecutive_one_count(array))
