# question asked at industrybuying

def longest_common_suffix(input_array):
    common_suffix = input_array[0]
    for item in input_array[1:]:
        while not item.endswith(common_suffix):
            common_suffix = common_suffix[1:]
            if not common_suffix:
                return ""
    return common_suffix


def longest_common_suffix_1(input_array):
    if len(input_array) == 0:
        return ""
    reversed_string = [s[::-1] for s in input_array]

    longest = reversed_string[0]
    for item in reversed_string[1:]:
        i = 0
        while i < len(item) and i < len(longest) and item[i] == longest[i]:
            i += 1
        longest = longest[:i]
    return longest[::-1]


if __name__ == '__main__':
    array = ['celebration', 'opinion', 'decision', 'revision']
    print(longest_common_suffix(array))
