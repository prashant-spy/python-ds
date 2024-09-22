# question asked in Fintech

# def target_sum(arr, target):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if j == len(arr) - 1:
#                 target_sums = arr[i]
#             else:
#                 target_sums = arr[i] + arr[j + 1]
#             if target == target_sums:
#                 return [i, j + 1]

def target_sum(arr, required_sum):
    n = len(arr)
    low = 0
    high = n - 1
    while low < high:
        total_sum = arr[low] + arr[high]
        if total_sum == required_sum:
            return low + 1, high + 1
        if total_sum > required_sum:
            high -= 1
        else:
            low += 1
    return -1, -1


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    # print(target_sum(nums, target))
    print(target_sum(nums, target))
