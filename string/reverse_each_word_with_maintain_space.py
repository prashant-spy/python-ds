def reverse_each_letter_with_maintain_space(input_str):
    words = input_str.split(" ")
    reversed_word = [word[::-1] for word in words]
    return " ".join(reversed_word)


if __name__ == '__main__':
    str = "Let's take LeetCode contest"
    print(reverse_each_letter_with_maintain_space(str))
