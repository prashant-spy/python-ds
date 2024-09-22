def find_avg_salary(nums):
    max_salary = nums[0]
    min_salary = nums[0]
    sum_salary = nums[0]

    for i in range(1,len(nums)):
        if max_salary < nums[i]:
            max_salary = nums[i]
        elif min_salary > nums[i]:
            min_salary = nums[i]
        sum_salary += nums[i]

    sum_salary = sum_salary - max_salary - min_salary
    avg_salary = float(sum_salary) / (len(nums)-2)

    return avg_salary


if __name__ == '__main__':
    salary = [4000,3000,1000,2000]
    expected = 2500.00000
    print(find_avg_salary(salary))