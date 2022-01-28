def solution(s):
    stack = list(s)
    out_stack = []
    while stack:
        temp = stack.pop()
        if not out_stack:
            out_stack.append(temp)
        else:
            if temp != out_stack[-1]:
                out_stack.append(temp)
            else:
                out_stack.pop()

    return 1 if not stack and not out_stack else 0


if __name__ == '__main__':
    result = 0
    s = "cdcd"
    solution_result = solution(s)
    print("Success" if result == solution_result else "Fail")
