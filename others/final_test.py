def reverse_each_word(input_string):
    out = []
    for c in input_string:
        if c.isupper():
            out.append(c)
    return "".join(out)


if __name__ == '__main__':
    """Check if a String Contains Only UPPERCASE """
    s = 'AuToMation'
    print(reverse_each_word(s))
