def find_second_element(array):
    """Find second most element in array"""

    largest = array[0]
    N = len(array)
    for i in range(N):
        if array[i] > largest:
            largest = array[i]

    second_largest = -1
    for i in range(N):
        if array[i] > second_largest and array[i] != largest:
            second_largest = array[i]
    return second_largest


def largest_arr(input_arr):
    """Optimal solution for find second most element array"""

    mx = max(input_arr[0], input_arr[1])
    second_max = min(input_arr[0], input_arr[1])
    n = len(input_arr)

    for i in range(n):
        if input_arr[i] > mx:
            mx = input_arr[i]
        elif second_max < input_arr[i] != mx:
            second_max = input_arr[i]
        elif mx == second_max and second_max != input_arr[i]:
            second_max = input_arr[i]
    return second_max


if __name__ == '__main__':
    arr = [1, 57, 24, 6, 2]
    print(find_second_element(arr))
    print(largest_arr(arr))
