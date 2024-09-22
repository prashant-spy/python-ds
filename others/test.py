# Input - ppournniima
# Number of sub-strings required = 3

def remove_k_duplicates(input_str, k):
    stack = []
    count_stack = []
    for char in input_str:
        if not stack or char != stack[-1][0]:
            stack.append((char, 1))
        else:
            count_stack[-1] += 1
            if count_stack[-1] == k:
                stack.pop()
                count_stack.pop()
        count_stack.append(1)

    return ''.join(char * count for char, count in stack)


# Example usage:
input_str = "abcbaacd"
k = 3
result = remove_k_duplicates(input_str, k)
print("Result after removing", k, "duplicates:", result)
