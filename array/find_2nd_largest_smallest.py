def find_2nd_largest_smallest(array):
    if len(array) < 2:
        return None, None

    first_largest = second_largest = float('-inf')
    first_smallest = second_smallest = float('inf')

    for num in array:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num

        elif first_largest > num > second_largest:
            second_largest = num

        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num

        elif first_smallest < num < second_smallest:
            second_smallest = num

    return second_largest, second_smallest


if __name__ == '__main__':
    arr = [12, 35, 1, 10, 34, 1]
    print(find_2nd_largest_smallest(arr))
