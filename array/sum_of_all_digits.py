# int = 1234
# sum of all digits - 10 two digit --- if it is not two digit -- 1+0 = 1

def sum_of_digit(n):
    if n == 0:
        return 0
    elif n % 9 == 0:
        return 9
    else:
        return n % 9


if __name__ == '__main__':
    num = 1234
    out = sum_of_digit(num)
    print(out)
