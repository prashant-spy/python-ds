def find_target_indices_after_sorting(array, target):
    num = 0
    target_count = 0

    for item in array:
        if item == target:
            target_count += 1
        elif item < target:
            num += 1

    result = []
    while target_count > 0:
        result.append(num)
        num += 1
        target_count -= 1

    return  result


if __name__ == '__main__':
    nums = [1, 2, 5, 2, 3]
    k = 2
    print(find_target_indices_after_sorting(nums, k))
