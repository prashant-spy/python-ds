def reverse(input_string, n):
    if n < 1:
        return ""

    if n == 1:
        return input_string[0]

    return input_string[n - 1] + reverse(input_string, n - 1)


if __name__ == '__main__':
    input_string = "geeks for geeks"
    n = len(input_string)
    print(reverse(input_string, n))
