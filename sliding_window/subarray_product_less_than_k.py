def subarray_product_less_than_k(nums, k):
    i = 0
    j = 0
    p = 1
    total_subarray = 0
    n = len(nums)

    while j < n:
        p *= nums[j]

        while p >= k:
            p = int(p // nums[j])
            i += 1

        if p < k:
            total_subarray += j - i + 1

        j += 1

    return total_subarray


if __name__ == '__main__':
    array = [1, 2, 3, 4]
    k = 10
    print(subarray_product_less_than_k(array, k))
