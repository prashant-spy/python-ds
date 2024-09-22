"""
Rearrange array elements by sign
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers
"""


def rearrange_by_sign(input_array):
    n = len(input_array)
    ans = [0] * n
    pos_index, neg_index = 0, 1
    for i in range(n):
        if input_array[i] < 0:
            ans[neg_index] = input_array[i]
            neg_index += 2
        else:
            ans[pos_index] = input_array[i]
            pos_index += 2
    return ans


if __name__ == '__main__':
    array = [1, 2, -3, 4, -2]
    out = rearrange_by_sign(array)
    print(out)
