def longest_palindromic_substring(input_string):
    if not input_string:
        return ''
    max_str = ''
    max_length = 0

    for i in range(len(input_string)):
        curr_str = expand_around_center(input_string, i, i)
        curr_length = len(curr_str)

        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str

        curr_str = expand_around_center(input_string, i, i + 1)
        curr_length = len(curr_str)
        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str

    return max_str


def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]


if __name__ == '__main__':
    s = "forgeeksskeegfor"
    print(longest_palindromic_substring(s))
