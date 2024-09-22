def longestPalindrome(input_string):
    n = len(input_string)
    if n == 0:
        return ""

    longest = ""
    for i in range(n):
        # Odd length palindromes
        odd_palindrome = expand_around_center(input_string, i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome

        # Even length palindromes
        even_palindrome = expand_around_center(input_string, i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest


def expand_around_center(input_string, left, right):
    while left >= 0 and right < len(input_string) and input_string[left] == input_string[right]:
        left -= 1
        right += 1
    return input_string[left + 1:right]


if __name__ == '__main__':
    s = "babad"
    print(longestPalindrome(s))
