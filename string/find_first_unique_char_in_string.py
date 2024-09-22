def find_first_unique_char_index(string):
    visited = set()
    n = len(string)
    for i in range(n):
        if string[i] not in visited and string.index(string[i]) == string.rindex(string[i]):
            return i
        visited.add(string[i])
    return -1


if __name__ == '__main__':
    s = "loveleetcode"
    print(find_first_unique_char_index(s))