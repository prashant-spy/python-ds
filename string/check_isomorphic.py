def check_isomorphic(string1, string2):
    if len(string1) != len(string2):
        return False

    mapp1 = {}
    mapp2 = {}

    for i in range(len(s)):
        if s[i] in mapp1:
            # Check if the current mapping is consistent
            if mapp1[s[i]] != t[i]:
                return False
        else:
            mapp1[s[i]] = t[i]

        if t[i] in mapp2:
            # Check if the current mapping is consistent
            if mapp2[t[i]] != s[i]:
                return False
        else:
            mapp2[t[i]] = s[i]

    return True


if __name__ == '__main__':
    s = "badc"
    t = "baba"
    print(check_isomorphic(s, t))
