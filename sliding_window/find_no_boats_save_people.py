# Leetcode questions - https://leetcode.com/problems/boats-to-save-people/description/

def find_number_of_boats(people, limit):
    people.sort()
    n = len(people)
    left = 0
    right = n - 1

    boats = 0

    while left <= right:
        weight = people[left] + people[right]

        if weight <= limit:
            left += 1

        boats += 1
        right -= 1

    return boats


if __name__ == '__main__':
    nums = [1, 2]
    k = 3
    print(find_number_of_boats(nums, k))
