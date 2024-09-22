
# https://leetcode.com/problems/three-consecutive-odds/description/
def find_three_consecutive_odd(nums):
    odd_count = 0
    for item in nums:
        if item % 2 != 0:
            odd_count += 1
        else:
            odd_count = 0
        if odd_count == 3:
            return True
    return True


if __name__ == '__main__':
    array = [1,2,34,3,4,5,7,23,12]
    print(find_three_consecutive_odd(array))