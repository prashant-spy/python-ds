def get_common(s1, s2):
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            return s1[i]
        elif s1[i] < s2[j]:
            i += 1
        else:
            j += 1
    return -1


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [2, 4]
    print(get_common(nums1, nums2))
