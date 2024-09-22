"""Find the longest unique substring from a string using sliding window
or
Find the longest substring without repeating char"""


def find_max_length_unique_substring(input_string):
    n = len(input_string)
    i = 0
    j = 0
    max_len = 0
    mapp = {}

    while j < n:
        mapp[input_string[j]] = mapp.get(input_string[j], 0) + 1

        if len(mapp) == j - i + 1:
            print(input_string[i:j + 1])
            max_len = max(max_len, j - i + 1)

        elif len(mapp) < j - i + 1:
            while len(mapp) < j - i + 1:
                mapp[input_string[i]] -= 1
                if mapp[input_string[i]] == 0:
                    del mapp[input_string[i]]
                i += 1
        j += 1
    return max_len


if __name__ == '__main__':
    array = "pwwkew"
    print(find_max_length_unique_substring(array))
