def reverse_each_letter_with_maintain_space(input_str):
    input_list = list(input_str)
    N = len(input_list)
    i = 0
    j = N - 1

    while i <= j:
        if input_list[i] == " ":
            i += 1
            continue
        elif input_list[j] == " ":
            j -= 1
            continue
        else:
            input_list[i], input_list[j] = input_list[j], input_list[i]
            i += 1
            j -= 1

    return " ".join(input_list)


if __name__ == '__main__':
    str = "i am a java guy"
    print(reverse_each_letter_with_maintain_space(str))
