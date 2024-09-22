def count_occurrence_of_anagram(string, pattern):
    n = len(string)
    k = len(pattern)
    mapp = {}

    for i in pattern:
        mapp[i] = mapp.get(i, 0) + 1

    count = len(mapp)
    i = 0
    j = 0
    ans = 0

    while j < n:
        if string[j] in mapp:
            mapp[string[j]] -= 1
            if mapp[string[j]] == 0:
                count -= 1

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            if count == 0:
                ans += 1
            if string[i] in mapp:
                mapp[string[i]] += 1
                if mapp[string[i]] == 1:
                    count += 1

            i += 1
            j += 1
    return ans


if __name__ == '__main__':
    string = "forxxorfxdofr"
    pattern = "for"
    print(count_occurrence_of_anagram(string, pattern))
