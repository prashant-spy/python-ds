""" bitonic array is an array whose one part is incresing and next part is decreasing"""


def check_bitonic_array(input_array):
    increasing = False
    decreasing = False
    n = len(input_array)

    if n < 3:
        return False

    for i in range(0, n - 1):
        if input_array[i] < input_array[i + 1]:
            increasing = True
        elif input_array[i] > input_array[i + 1]:
            decreasing = True

        if increasing and decreasing:
            return True
    return False


if __name__ == '__main__':
    array = [2, 0, 2]
    print(check_bitonic_array(array))
