def find_all_duplicates(array):
    mapp = {}
    result = []
    for item in array:
        mapp[item] = mapp.get(item, 0) + 1

    for item, value in mapp.items():
        if value > 1:
            result.append(item)

    return result


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(find_all_duplicates(nums))
