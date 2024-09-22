def find_first_index_occurence_string(input_string, pattern):
    n = len(input_string)
    k = len(pattern)

    for i in range(n - k + 1):
        if input_string[i:i + k] == pattern:
            return i
    return -1


if __name__ == '__main__':
    haystack = "mississippi"
    needle = "pi"
    print(find_first_index_occurence_string(haystack, needle))
