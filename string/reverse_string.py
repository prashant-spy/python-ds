def reverse(l, r):
    string = list('madam')
    if l >= r:
        return
    else:
        string[l], string[r] = string[r], string[l]
        reverse(l + 1, r - 1)
    return "".join(string)


if __name__ == '__main__':
    strr = 'madam'
    l = 0
    r = len(strr) - 1
    print(reverse(l, r))
