def remove_duplicate(array, num):
    if num == 0 or num == 1:
        return num
    temp_variable = list(range(num))

    j = 0
    for item in range(0, num - 1):
        if array[item] != array[item + 1]:
            temp_variable[j] = array[item]
            j += 1
    temp_variable[j] = array[num - 1]
    j += 1

    for item in range(0, j):
        array[item] = temp_variable[item]
    return j


def subset_check(array_1, array_2):
    result = all(x in array_1 for x in array_2)
    print(result)


if __name__ == "__main__":
    input_arr = [10, 10, 7, 10, 3, 15, 1000, 7]
    input_1 = [7, 1000, 15]
    input_2 = [7, 1000, 15, 7, 15, 1]

    subset_check(input_arr, input_1)
    subset_check(input_arr, input_2)

    input_arr.sort()
    n = len(input_arr)
    out = remove_duplicate(input_arr, n)
    temp = []
    for i in range(out):
        temp.append(input_arr[i])
    print(temp)
