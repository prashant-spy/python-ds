def check_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    mapp = {}
    for i in str1:
        mapp[i] = mapp.get(i, 0) + 1

    for j in str2:
        if j in mapp:
            mapp[j] -= 1
        else:
            return False

    keys = mapp.keys()
    for key in keys:
        if mapp[key] != 0:
            return False
    return True


if __name__ == '__main__':
    input1 = "listen"
    input2 = "silent"

    output = check_anagram(input1, input2)
    if output:
        print("word are anagram")
    else:
        print("word not an anagram")
