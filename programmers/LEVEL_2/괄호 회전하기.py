def solution(s):
    answer = 0
    stack = []
    for i in range(len(s)):
        temp_str = s[i:] + s[0:i]
        if stack_check(list(temp_str)):
            answer += 1
    return answer


def stack_check(stack):
    temp_stack = [stack.pop(0)]
    while stack:
        temp = stack.pop(0)
        if temp_stack:
            if temp_stack[-1] == '(' and temp == ')':
                temp_stack.pop()
            elif temp_stack[-1] == '[' and temp == ']':
                temp_stack.pop()
            elif temp_stack[-1] == '{' and temp == '}':
                temp_stack.pop()
            else:
                temp_stack.append(temp)
        else:
            temp_stack.append(temp)

    return len(temp_stack) == 0


if __name__ == '__main__':
    result = 2
    s = "}]()[{"
    solution_result = solution(s)
    print("Success" if result == solution_result else "Fail")
