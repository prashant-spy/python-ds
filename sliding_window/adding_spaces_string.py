"""given s = "EnjoyYourCoffee" and spaces = [5, 9],
 we place spaces before 'Y' and 'C', which are at indices 5 and 9
 respectively. Thus, we obtain "Enjoy Your Coffee""
 """


def add_spaces(input_string, spaces):
    result = []
    space_index = 0
    spaces_length = len(spaces)

    for i in range(len(input_string)):
        if space_index < spaces_length and i == spaces[space_index]:
            result.append(' ')
            space_index += 1
        result.append(input_string[i])

    return ''.join(result)


if __name__ == '__main__':
    s = "LeetcodeHelpsMeLearn"
    spaces = [8, 13, 15]
    print(add_spaces(s, spaces))
