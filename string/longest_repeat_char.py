# question asked in Fintech

def longest_repeat_char(input_str):
    n = len(input_str)
    res = 0
    for i in range(n):
        for j in range(i, n):
            if distinct_check(input_str, i, j):
                res = max(res, j - i + 1)
    return res


def distinct_check(input_str, i, j):
    visited = [0] * 256
    for k in range(i, j + 1):
        if visited[ord(input_str[k])]:
            return False
        visited[ord(input_str[k])] = True
    return True


if __name__ == '__main__':
    string = "bbbbbaaacr"
    length = longest_repeat_char(string)
    print("length of longest repeating char substring is ", length)
