def move_all_zeros(input_array):
    left = 0
    for right in range(len(input_array)):
        if input_array[right] != 0:
            input_array[right], input_array[left] = input_array[left], input_array[right]
            left += 1
    return input_array


if __name__ == '__main__':
    array = [0, 1, 0, 3, 12, 122, 0, 1, 0, 1]
    print(move_all_zeros(array))
