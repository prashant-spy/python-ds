"""2 sum problem to check array if sum of 2 element is equal to target"""


def sum_problem(array, N, target):
    for i in range(N):
        for j in range(N):
            if array[i] + array[j] == target:
                return True
    return False


"""2 sum problem to check array if sum of 2 element is equal to target"""
"""alternative way with O(N)"""


def two_sum_problem(arr, target):
    complements = dict()

    for index, number in enumerate(arr):
        complement = target - number
        if complement in complements:
            return [complements[complement], index]
        complements[number] = index
    return [-1, -1]


if __name__ == '__main__':
    array = [2, 6, 5, 8, 11]
    N = 5
    target = 14
    # result = sum_problem(array, N, target)
    result = two_sum_problem(array, target)
    print(result)
