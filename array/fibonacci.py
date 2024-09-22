def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == "__main__":
    n = 10
    for i in range(n):
        print(fibonacci(i), end=" ")
