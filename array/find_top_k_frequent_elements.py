from collections import Counter


def find_top_k_frequent_element(array, k):
    array_count = Counter(array)
    elements = []

    element_count = 1
    sorted_data = sorted(array_count.items(), key=lambda x: x[1], reverse=True)

    for item,value in sorted_data:
        if element_count <= k:
            elements.append(item)
            element_count += 1
    return elements


if __name__ == '__main__':
    nums = [4, 1, -1, 2, -1, 2, 3]
    k = 2
    print(find_top_k_frequent_element(nums, k))
