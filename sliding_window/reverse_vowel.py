# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

def reverse_vowels(s):
    s_list = list(s)
    n = len(s_list)
    left = 0
    right = n - 1

    while left < right:
        if not is_vowel(s_list[left]):
            left += 1
        elif not is_vowel(s_list[right]):
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

    return "".join(s_list)


def is_vowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']


if __name__ == '__main__':
    string = "hello"
    output = "holle"
    print(reverse_vowels(string))
