# asked in mai.io 2nd round
def print_prime_number(start, end):
    prime_list = []
    for i in range(start, end):
        if i <= 1:
            continue
        else:
            for j in range(2, int(i / 2) + 1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list


if __name__ == '__main__':
    start = 1
    end = 100
    out = print_prime_number(start, end)
    for item in out:
        print(item)

number_list = [1, 2, 3, 1, 2, 3]

# output = [n for n in number_list if n % 2 == 0]

output_new = []
output = [output_new.append(i) for i in number_list if i not in output_new]
print(output_new)

# select * from employee order by created at desc limit 100;


# insert into employee name ,email,salary value ("test","test.asas@gmail.com",121212);
