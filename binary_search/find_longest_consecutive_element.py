def longest_consecutive_array(arr):
    """Finding the longest consecutive array in better approach"""
    N = len(arr)
    if N == 0:
        return 0
    arr.sort()
    last_smaller = float('-inf')
    cnt = 0
    longest = 1

    for i in range(N):
        if arr[i] - 1 == last_smaller:
            cnt += 1
            last_smaller = arr[i]
        elif arr[i] != last_smaller:
            cnt = 1
            last_smaller = arr[i]
        longest = max(longest, cnt)
    return longest


if __name__ == '__main__':
    array = [100, 200, 1, 2, 3, 4, 5]
    print(longest_consecutive_array(array))
