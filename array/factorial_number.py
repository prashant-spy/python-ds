def factorial_number(n):
    if n == 0:
        return 1
    return n * factorial_number(n - 1)


if __name__ == '__main__':
    n = 6
    print(factorial_number(n))
