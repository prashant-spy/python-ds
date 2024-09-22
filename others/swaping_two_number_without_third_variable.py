def swapping_of_number(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2

    print(num1, num2)


if __name__ == '__main__':
    a = 12
    b = 10
    swapping_of_number(a, b)
