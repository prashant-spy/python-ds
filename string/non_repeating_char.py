# name = "gagan"

# non repeating char
# question asked by brightly

def non_repeating_char(name):
    for i in name:
        if name.find(i, (name.find(i) + 1)) == -1:
            print("non repeating char", i)
            break
    return


if __name__ == '__main__':
    name = "gagank"
    non_repeating_char(name)
