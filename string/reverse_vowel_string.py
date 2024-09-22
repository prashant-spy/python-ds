def reverse_vowel_of_string(string):
    vowels = "aeiouAEIOU"
    s_list = list(string)
    n = len(s_list)

    left = 0
    right = n - 1

    while left < right:
        if not s_list[left] in vowels:
            left += 1
        elif not s_list[right] in vowels:
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    return "".join(s_list)


if __name__ == '__main__':
    s = "helloai"
    print(reverse_vowel_of_string(s))
