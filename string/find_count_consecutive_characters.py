def find_count_consecutive_characters(input_string):
    count = 1
    max_count = 1

    for i in range(1, len(input_string)):
        curr = input_string[i]
        prev = input_string[i - 1]

        if curr == prev:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1
    max_count = max(max_count, count)
    return max_count


if __name__ == '__main__':
    s = "leetcode"
    print(find_count_consecutive_characters(s))
