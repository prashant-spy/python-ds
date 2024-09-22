def reverse_string(input_str):
    input_str = list(input_str)
    N = len(input_str)
    i = 0
    j = N - 1
    while i <= j:
        if not input_str[i].isalpha():
            i += 1
            continue
        elif not input_str[j].isalpha():
            j -= 1
            continue
        else:
            input_str[i], input_str[j] = input_str[j], input_str[i]
            i += 1
            j -= 1
    return "".join(input_str)


if __name__ == '__main__':
    input_string = 'a,b$c'
    output_string = 'c,b$a'
    print(reverse_string(input_string))
