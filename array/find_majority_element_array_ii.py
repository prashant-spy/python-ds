# https://leetcode.com/problems/majority-element-ii/description
from collections import Counter


def find_majority_element(array):
    element_count = Counter(array)

    majority_element = []
    threshold = len(array) // 3

    for element, count in element_count.items():
        if count > threshold:
            majority_element.append(element)
    return majority_element


if __name__ == '__main__':
    nums = [3, 2, 3]
    print(find_majority_element(nums))
