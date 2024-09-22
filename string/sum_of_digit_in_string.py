import re


def sum_of_digit_string(nums):
    total_sum = 0
    for i in nums:
        if i.isdigit():
            total_sum += int(i)
    return total_sum


def sum_of_digit_strings(s):
    s_list = re.findall(r'\d+', s)
    total_sum = 0
    for num in s_list:
        total_sum += int(num)
    return total_sum


if __name__ == '__main__':
    s = '23sdsdf 25nanajs 24 anksans'
    print(sum_of_digit_strings(s))
