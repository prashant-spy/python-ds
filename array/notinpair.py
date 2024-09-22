# not in pair
# question asked by brightly

def not_in_pair(input, n):
    result = input[0]
    for i in range(1, n):
        result = result ^ input[i]
    return result


if __name__ == '__main__':
    test_input = "1144223558"
    test_input = list(test_input)
    n = 2
    out = not_in_pair(test_input, 2)
