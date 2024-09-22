"""You are given an integer n. If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1 to it.
Continue this process until n becomes 1"""


def collaz_conjecture(num):
    while num != 1:
        print(num, end="")
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
    return num


if __name__ == '__main__':
    n = 6
    print(collaz_conjecture(n))
