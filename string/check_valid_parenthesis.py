def check_valid_parenthesis(s):
    stack = []
    lookup = {")": "(", "}": "{", "]": "["}
    for item in s:
        if item in lookup.values():
            stack.append(item)
        elif item in lookup:
            if len(stack) == 0 or stack.pop() != lookup[item]:
                return False
        else:
            return False
    return len(stack) == 0


if __name__ == '__main__':
    input_str = "()[]{}"
    print(check_valid_parenthesis(input_str))
