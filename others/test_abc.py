# target_string - Prashant
# longest substring without repeating char asked in slice

# op- prash/shant


def longest_substring(input_string):
    n = len(input_string)
    result = 0

    for i in range(n):
        for j in range(i, n):
            if distinct_check(input_string, i, j):
                length = len(input_string[i:j+1])
                result = max(result, j - i + 1)
                if length == result:
                    print(input_string[i:j+1])

    return result


def distinct_check(input_string, i, j):
    visited = [0] * 256
    for item in range(i, j + 1):
        if visited[ord(input_string[item])]:
            return False
        visited[ord(input_string[item])] = True
    return True


if __name__ == '__main__':
    string = 'prashant'
    print(longest_substring(string))
