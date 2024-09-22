
# Find missing number from a sorted array using BS
def find_missing_number(input_array):

    n = len(input_array)
    left = 0
    right = n - 1

    while left < right:
        mid = left + right // 2

        if input_array[mid] - mid == input_array[0]:

            if input_array[mid + 1] - input_array[mid] > 1:
                return input_array[mid] + 1
            else:
                left = mid + 1
        else:
            if input_array[mid] - input_array[mid - 1] > 1:
                return input_array[mid] - 1
            else:
                right = mid - 1

    return -1


if __name__ == '__main__':
    array = [0, 1, 2, 6, 9, 11, 15]
    print(find_missing_number(array))
