from collections import defaultdict


def group_anagrams(input_strs):
    anagrams = defaultdict(list)

    for word in input_strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)

    return list(anagrams.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    print(group_anagrams(strs))
