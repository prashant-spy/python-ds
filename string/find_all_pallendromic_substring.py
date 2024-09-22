def find_all_palindromic_substring(input_str):
    palindromes = set()
    for i in range(len(input_str)):
        expand_around_center(input_str, i, i, palindromes)
        expand_around_center(input_str, i, i + 1, palindromes)

    return palindromes


def expand_around_center(s, left, right, palindromes):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        palindromes.add(s[left:right + 1])
        left -= 1
        right += 1


if __name__ == '__main__':
    s = 'google'
    print(find_all_palindromic_substring(s))
