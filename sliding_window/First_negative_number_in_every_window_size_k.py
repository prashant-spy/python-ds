from collections import deque


def first_negative_number_window(input_arr, k):
    n = len(input_arr)
    negative_indexes = deque()
    for i in range(n):
        if negative_indexes and negative_indexes[0] == i - k:
            negative_indexes.popleft()
        if input_arr[i] < 0:
            negative_indexes.append(i)

        if i >= k - 1:
            if negative_indexes:
                print(input_arr[negative_indexes[0]], end=",")
            else:
                print("0")


if __name__ == '__main__':
    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    k = 3
    first_negative_number_window(arr, k)
