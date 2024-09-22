"""Given a string s consisting only of characters 'a', 'b', and 'c'.
You are asked to apply the following algorithm on the string any number of times
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".
"""


def min_length(input_string):
    N = len(s)
    i = 0
    j = N - 1

    while i < j:
        if input_string[i] == input_string[j]:
            char = input_string[i]

            while i <= j and input_string[i] == char:
                i += 1
            while j >= i and input_string[j] == char:
                j -= 1
        else:
            break
    return j - i + 1


if __name__ == '__main__':
    s = 'aabccabba'
    print(min_length(s))
