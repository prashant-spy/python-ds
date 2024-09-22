def find_max_repeating_substring(strr, k):
    max_k = 0
    i = 1

    while i * k in strr:
        max_k = i
        i += 1

    return max_k


if __name__ == '__main__':
    sequence = "ababc"
    word = "ab"
    print(find_max_repeating_substring(sequence, word))
