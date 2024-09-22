def find_majority_element_duplicate_array(array):
    res = majority = 0
    for i in array:
        if majority == 0:
            res = i
        majority += 1 if i == res else -1
    return res


if __name__ == '__main__':
    nums = [6, 5, 5]
    print(find_majority_element_duplicate_array(nums))
