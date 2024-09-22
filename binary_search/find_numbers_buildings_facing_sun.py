def count_buildings_facing_sun(nums):
    count = 1
    curr_max = nums[0]
    n = len(nums)
    for i in range(1, n):
        if nums[i] > curr_max or nums[i] == curr_max:
            count += 1
            curr_max = nums[i]
    return count


if __name__ == '__main__':
    array = [7, 4, 8, 2, 9]
    print(count_buildings_facing_sun(array))
