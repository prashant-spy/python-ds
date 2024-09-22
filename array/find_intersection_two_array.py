

def intersection(array1, array2):
    return list(set(array1) & set(array2))


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersection(nums1, nums2))
