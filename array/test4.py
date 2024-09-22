# Asked in brightly
# string = "aabbccddaabbccee"
# a-2,b-2 c-2, d-1,e-1

def count_of_data(string):
    all_freq = {}
    for i in string:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    first_non_repeated = None
    first_repeated = None

    for key, value in all_freq.items():
        if value == 1 and first_non_repeated is None:
            first_non_repeated = key
        elif value > 1 and first_repeated is None:
            first_repeated = key

        if first_non_repeated and first_repeated:
            break

    if first_non_repeated:
        print(f"First non-repeated element: {first_non_repeated}")
    else:
        print("No non-repeated element found.")

    if first_repeated:
        print(f"First repeated element: {first_repeated}")
    else:
        print("No repeated element found.")


if __name__ == '__main__':
    input_str = "aabbccddfaabbccee"
    count_of_data(input_str)
