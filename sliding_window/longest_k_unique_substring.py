"""Longest Substring with At Most K Distinct Characters"""


def longest_k_unique_substring(input_str, k):
    n = len(input_str)
    i = 0
    j = 0
    max_len = 0
    mapp = {}

    while j < n:
        mapp[input_str[j]] = mapp.get(input_str[j], 0) + 1

        if len(mapp) == k:
            print(input_str[i:j + 1])
            max_len = max(max_len, j - i + 1)

        elif len(mapp) > k:
            while len(mapp) > k:
                mapp[input_str[i]] -= 1
                if mapp[input_str[i]] == 0:
                    del mapp[input_str[i]]
                i += 1
        j += 1
    return max_len


if __name__ == '__main__':
    strr = "abbbbbbcc"
    k = 2
    print(longest_k_unique_substring(strr, k))
