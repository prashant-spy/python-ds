def first_unique_char(input_string):
    mapp = {}
    for char in input_string:
        if char in mapp:
            mapp[char] += 1
        else:
            mapp[char] = 1

    for index, char in enumerate(input_string):
        if mapp[char] == 1:
            return index
    return -1


if __name__ == '__main__':
    s = "loveleetcode"
    print(first_unique_char(s))
