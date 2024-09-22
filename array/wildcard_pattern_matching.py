# ? can match to any single character
# * can match to any number of characters including zero characters


# Input:  string = “xyxzzxy”, pattern = “x***y”
# Output: Match

# Input:  string = “xyxzzxy”, pattern = “x***x”
# Output: No Match
#
# Input:  string = “xyxzzxy”, pattern = “x***x?”
# Output: Match
#
# Input:  string = “xyxzzxy”, pattern = “*”
# Output: Match


"""Ref redbus Wildcard Pattern Matching
"""


def check_match(input_string, pattern):
    n = len(input_string)
    m = len(pattern)
    if m == 0:
        return n == 0
    lookup = [[False for i in range(m + 1)] for j in range(n + 1)]
    lookup[0][0] = True

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[j - 1] == "*":
                lookup[0][j] = lookup[0][j - 1] or lookup[i - 1][j]
            elif pattern[j - 1] == "?" or input_string[i - 1] == pattern[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1]
            else:
                lookup[i][j] = False

    return lookup[n][m]


if __name__ == '__main__':
    string = 'xyxzzxy'
    k = "x***y"
    if check_match(string, k):
        print("Match")
    else:
        print("Not Matched")
