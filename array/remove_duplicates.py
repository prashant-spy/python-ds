"""Remove Duplicates from Sorted Array"""


def remove_duplicates(input_array):
    n = len(input_array)
    if n <= 1:
        return n

    last_index = 0
    for index in range(1, n):
        if input_array[index] != input_array[last_index]:
            last_index += 1
            input_array[last_index] = input_array[index]

    return input_array[:last_index+1]


if __name__ == '__main__':
    array = [1, 2, 2, 3, 4, 5, 6, 6, 8]
    print(remove_duplicates(array))
