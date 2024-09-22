def swap_adjacent_chars(string):
    s_list = list(string)
    n = len(s_list)

    i = 0
    j = n - 1

    while i < j:
        if s_list[i] != " " and s_list[i + 1] != " ":
            s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
            i += 2
        else:
            i += 1

    return "".join(s_list)


if __name__ == '__main__':
    s = "I love my country"
    print(swap_adjacent_chars(s))
