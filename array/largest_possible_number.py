# question asked in grayorange

from functools import cmp_to_key


def largest_possible_number(input_array):
    result = sorted(input_array, key=cmp_to_key(compare))
    return "".join(map(str, result))


def compare(Key1, Key2):
    ab = int(str(Key1) + str(Key2))
    ba = int(str(Key2) + str(Key1))

    if ab > ba:
        return -1
    elif ab < ba:
        return 1
    else:
        return 0


if __name__ == '__main__':
    array = [3, 30, 34, 5, 9]
    print(largest_possible_number(array))
