# question asked in wolter kluwers 2nd round

def find_occurrence(input_name):
    mapp = {}
    for n in input_name:
        if n in mapp:
            mapp[n] += 1
        else:
            mapp[n] = 1
    return mapp


if __name__ == '__main__':
    name = "prashant barik"
    out = find_occurrence(name)
    print(out)
