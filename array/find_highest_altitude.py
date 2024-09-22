def find_highest_altitude(nums):
    max_height = 0
    gain_height = 0

    for i in range(len(nums)):
        gain_height += nums[i]
        max_height = max(max_height,gain_height)
    return max_height


if __name__ == '__main__':
    gain = [-5, 1, 5, 0, -7]
    print(find_highest_altitude(gain))