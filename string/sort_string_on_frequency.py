def sort_string_on_frequency(string):
    list_string = list(string)
    mapp = {}
    for item in list_string:
        mapp[item] = mapp.get(item, 0) + 1

    sorted_arr = sorted(list_string, key=lambda x: (-mapp[x] , x))
    return "".join(char.lower() for char in sorted_arr)


if __name__ == '__main__':
    s = 'Kapoor'
    print(sort_string_on_frequency(s))
