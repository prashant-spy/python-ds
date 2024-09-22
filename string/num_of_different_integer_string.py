import re


def count_unique_integer_string(word):
    digit = re.findall(r'[1-9]+', word)
    nums_set = set(digit)
    return len(nums_set)



if __name__ == '__main__':
    word = 'a1b01c001'
    print(count_unique_integer_string(word))
