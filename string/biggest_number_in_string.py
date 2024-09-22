def biggest_number_string(string):
    largest_number = ""
    for i in string:
        if i.isdigit() and int(i) > largest_number:
            largest_number = int(i)

    return largest_number


if __name__ == '__main__':
    s = "525"
    print(biggest_number_string(s))
