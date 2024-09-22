# Given an input array , Sort the values based on the occurrence of digits in ascending order.
# i/p: {2,6,6,2,1,2}
# o/p: {1,6,6,2,2,2}


def sort_occurance(arr):
    mapp = {}
    for i in arr:
        mapp[i] = mapp.get(i, 0) + 1

    sorted_arr = sorted(arr, key=lambda x: (mapp[x], x))
    return sorted_arr


if __name__ == '__main__':
    # input_arr = [2, 6, 6, 2, 1, 2]
    input_arr = [3,5,6,3,5]
    print(sort_occurance(input_arr))
