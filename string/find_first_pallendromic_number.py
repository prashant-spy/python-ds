def first_palindrome(words):
    output = ""
    for item in words:
        if item == item[::-1]:
            output = item
            break
    return output


if __name__ == '__main__':
    s = ["abc", "car", "ada", "racecar", "cool"]
    print(first_palindrome(s))
