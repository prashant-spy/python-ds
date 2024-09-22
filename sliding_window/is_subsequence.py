
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
def is_subseqence(pattern, input_string):
    i = 0
    j = 0
    while i < len(pattern) and j < len(input_string):
        if pattern[i] == input_string[j]:
            i += 1
        j += 1

    return i == len(pattern)


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    print(is_subseqence(s, t))
