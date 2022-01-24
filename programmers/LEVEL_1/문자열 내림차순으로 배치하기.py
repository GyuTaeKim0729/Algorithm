def solution(s):
    temp = list(s)
    temp.sort(reverse=True)
    answer = ''.join(temp)
    return answer


if __name__ == '__main__':
    result = "gfedcbZ"
    s = "Zbcdefg"
    solution_result = solution(s)
    print("Success" if result == solution_result else "Fail")
