def check_primenumber(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):  # 2 to n/2
            if num % i == 0:
                print(num, "number is not prime")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "number is not prime number")


if __name__ == '__main__':
    n = 3
    check_primenumber(n)

# time_complexity - O(n)
# aux-space - O(1)

# xpath wolter kluwer
# //strong[contains(text(),"Japan")]/following::td[contains(text(),"Tokyo") or contains(text(),"Yen") or contains(text(),"Japanese")]
