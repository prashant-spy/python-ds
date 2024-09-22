def longest_substring(str_list):
    length = len(str_list)

    if length == 0:
        return ""
    if length == 1:
        return str_list[0]

    str_list.sort()
    str_end = min(len(str_list[0]), len(str_list[length - 1]))
    i = 0
    while i < str_end and str_list[0][i] == str_list[length - 1][i]:
        i += 1
    pre = str_list[0][0:i]
    return pre


if __name__ == '__main__':
    str_list = ["flower", "flow", "flight"]
    print(longest_substring(str_list))
