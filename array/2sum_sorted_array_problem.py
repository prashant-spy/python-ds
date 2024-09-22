def twosum(input_numbers, target_number):
    n = len(input_numbers)
    left = 0
    right = n - 1
    while left < right:
        total_sum = input_numbers[left] + input_numbers[right]
        if total_sum < target_number:
            left += 1
        elif total_sum > target_number:
            right -= 1
        else:
            return [left + 1, right + 1]


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    print(twosum(numbers, target))
