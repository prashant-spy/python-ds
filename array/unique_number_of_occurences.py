def unique_number_of_occurrences(arr):
    mapp = {}
    for num in arr:
        nums[num] = mapp.get(num, 0) + 1

    occurrences = set()
    for i in mapp.values():
        if i in occurrences:
            return False
        occurrences.add(i)
    return True


if __name__ == '__main__':
    nums = [1, 2, 2, 1, 1, 3]
    print(unique_number_of_occurrences(nums))
