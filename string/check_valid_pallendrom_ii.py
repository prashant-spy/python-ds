def check_valid_palindrome(s):
    n = len(s)
    i = 0
    j = n - 1

    while i <= j:
        if s[i] != s[j]:
            string1 = s[:i] + s[i + 1:]
            string2 = s[:j] + s[j + 1:]
            return string1 == string1[::-1] or string2 == string2[::-1]
        return True


if __name__ == '__main__':
    str = "abca"
    print(check_valid_palindrome(str))
