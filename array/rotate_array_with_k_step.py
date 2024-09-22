def left_rotate_array_with_k_step(input_array, d):
    n = len(input_array)
    d = d % n  # to handle case where d >= n
    reverse_array(input_array, 0, d - 1)
    reverse_array(input_array, d, n - 1)
    reverse_array(input_array, 0, n - 1)

    return input_array


def right_rotate_with_k_steps(input_array, d):
    n = len(input_array)
    d = d % n
    reverse_array(input_array, 0, n - 1)
    reverse_array(input_array, 0, d - 1)
    reverse_array(input_array, d, n - 1)
    return input_array


def reverse_array(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6]
    k = 4
    print(left_rotate_array_with_k_step(array, k))
    print(right_rotate_with_k_steps(array, k))
