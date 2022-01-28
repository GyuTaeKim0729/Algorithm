def solution(p):
    answer = ''
    right_cnt = 0
    temp_str = ''
    for i in range(len(p)):
        if p[i] == '(':
            right_cnt += 1
        else:
            right_cnt -= 1
        temp_str += p[i]

        if right_cnt == 0:
            if temp_str[0] == ')':
                reorder = '('
                reorder += solution(p[i+1:])
                reorder += ')'
                for k in temp_str[1:-1]:
                    if k == '(':
                        reorder += ')'
                    else:
                        reorder += '('
                return reorder
            else:
                return temp_str + solution(p[i+1:])

    return answer


if __name__ == '__main__':
    result = "()(())()"
    p = "()))((()"
    solution_result = solution(p)
    print(solution_result)
    print("Success" if result == solution_result else "Fail")
