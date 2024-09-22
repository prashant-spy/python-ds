"""WAP to check string is palindrome or not
"""


def palindrome_check(input_string, start_index, end_index):
    if start_index == end_index:
        return True

    if input_string[start_index] != input_string[end_index]:
        return False

    if start_index < end_index:
        return palindrome_check(input_string, start_index + 1, end_index - 1)

    return True


if __name__ == '__main__':
    string = "geeg"
    n = len(string)
    start = 0
    end = n - 1

    out = palindrome_check(string, start, end)

    if out:
        print("yes")
    else:
        print("no")
