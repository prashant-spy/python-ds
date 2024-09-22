def string_compression(input_string):
    if not input_string:
        return ""

    mapp = {}
    for item in input_string:
        mapp[item] = mapp.get(item, 0) + 1

    final_output = []
    for key, value in mapp.items():
        final_output.append(key + str(value))

    return ''.join(final_output)


if __name__ == '__main__':
    string = "aabbcdaav"
    output = "a4b2c1d1v1"
    print(string_compression(string))

