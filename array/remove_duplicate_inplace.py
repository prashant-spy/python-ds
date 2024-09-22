"""Remove duplicate from inplace sorted array"""


def remove_duplicate(arr):
    n = len(arr)
    i = 0
    for j in range(n):
        if arr[j] != arr[i]:
            arr[i + 1] = arr[j]
            i += 1
    return arr[:i+1]


if __name__ == '__main__':
    array = [1, 1, 2, 2, 2, 2, 3, 3, 3]
    print(remove_duplicate(array))
