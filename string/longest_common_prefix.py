def longest_common_prefix(input_array):
    common_prefix = input_array[0]

    for item in input_array[1:]:
        while not item.startswith(common_prefix):
            common_prefix = common_prefix[:-1]
            if not common_prefix:
                return ""
    return common_prefix


if __name__ == '__main__':
    array = ["flower", "flow", "flight"]
    print(longest_common_prefix(array))
