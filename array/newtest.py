# Input : Hi, I am Prashant Barik
# Output : ,iH I ma tnahsarP kiraB

# 1. question asked in pocketFM

def reverse_sentence(string):
    s = string.split()
    new_words = [word[::-1] for word in s]
    new_sentence = " ".join(new_words)
    print(new_sentence)


if __name__ == '__main__':
    input_string = "Hi, I am Prashant Barik"
    reverse_sentence(input_string)

