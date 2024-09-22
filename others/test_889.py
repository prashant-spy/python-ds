# Longest substring repeating more than once in a given string .
# appleappleapp

# output - appleapp

# def longest_substring(input_string):
#     n = len(input_string)
#
#     str_1 = ""
#
#     for i in range(0, n):
#         for j in range(i + 1, n):
#             x = lcp(input_string[i:n], input_string[j:n])
#
#             if len(x) > len(str_1):
#                 str_1 = x
#     print(str_1)
#
#
# def lcp(input_1, input_2):
#     n = min(len(input_1), len(input_2))
#
#     for i in range(0, n):
#         if input_1[i] != input_2[i]:
#             return input_1[0:i]
#         else:
#             return input_1[0:n]
#
#
# if __name__ == '__main__':
#     input_string = "appleappleapp"
#     longest_substring(input_string)

# def longestDupSubstring(s):
#     #     """
#     #         This problem can be solved using Sliding Window Technique.
#     #         Logic:
#     #             1. Iterate over the string from 0th index
#     #             2. For each index, define a window of 1 initially.
#     #             3. Check for the existence of the window in the remaining string:
#     #                 a. If found, increase the size of window by 1 and repeat.
#     #                 b. Else Goto next index. For next index, the size window will not start by 1 again as we have already found for 1. So for every next index, size of window will start from the size at previous index to avoid checking for repeating size.
#     #     """
#     ans = ""
#     j = 1
#     for i in range(len(s)):
#         window = s[i:i + j]
#         heystack = s[i + 1:]
#         while window in heystack:
#             ans = window
#             j += 1
#             window = s[i:i + j]
#         return ans
#
#
# if __name__ == '__main__':
#     input_string = "appleappleapp"
#     print(longestDupSubstring(input_string))

# salary
# dept
# emp_id

# select department_id,sum(salary) from employees group by department_id;


# Emp Id , Dept , Toal Salaty , % of Salary of Emp_id of total salary of department

# select Emp_id, dept,100*sum(salary) / (sum(sum(salary)) over ()) as percentage
# from employee
# group by Emp_id;


# Problem: Finding the Longest Palindromic Substring in a Given String
# Description:
# Given a string, find the longest substring that is a palindrome. A palindrome is a string that reads the same forwards and backwards.

# Input: babad
# Output: bab or aba (both are correct)


def longest_pallendromic(input_str):
    n = len(input_str)
    max_len = 1
    start = 0
    for i in range(n):
        for j in range(i, n):
            flag = 1

            for k in range(0, (j - i) // 2 + 1):
                if input_str[i + k] != input_str[j - k]:
                    flag = 0
            if flag != 0 and j - i + 1 > max_len:
                start = i
                max_len = j - i + 1

    for i in range(start, start + max_len - 1 + 1):
        print(input_str[i], end="")

    return max_len


if __name__ == '__main__':
    input_str = "aabaaa"
    longest_pallendromic(input_str)
