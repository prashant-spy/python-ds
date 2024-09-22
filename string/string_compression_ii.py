"""Given a string with lower case, upper case and special characters, the resultant string should have the count of
character with each character separately.

Example: aaaAAab^B&bbc$cC%ca*aDdDd@bB
output: a6b4c4a2d4b2"""


def string_compression_ii(string):
    count = 1
    i = 0
    n = len(string)
    out = []

    while i < n:
        while i < n - 1 and not string[i].lower().isalpha():
            i += 1
        j = i + 1

        while j < n:
            if not string[j].lower().isalpha():
                j += 1
            elif string[i].lower() == string[j].lower():
                j += 1
                count += 1
            else:
                break

        out.append(string[i].lower() + str(count))
        count = 1
        i = j
    return "".join(out)


if __name__ == '__main__':
    s = "aaaAAab^B&bbc$cC%ca*aDdDd@bB"
    print(string_compression_ii(s))
