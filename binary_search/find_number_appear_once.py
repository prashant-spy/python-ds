def find_number_appears_once(input_arr):
    """Hashing method to find number with once appearance"""

    hash_map = {}
    for item in input_arr:
        hash_map[item] = hash_map.get(item, 0) + 1

    for item, count in hash_map.items():
        if count == 1:
            return item
    return -1


if __name__ == '__main__':
    arr = [1, 2, 1, 3, 3, 4, 4, 4]
    result = find_number_appears_once(arr)
    print(result)
