def solution(n):
    answer = 0
    temp_cnt = 0
    for j in range(60):
        for k in range(60):
            temp = str(j)+str(k)
            if temp.count('3') != 0:
                temp_cnt += 1

    for i in range(n+1):
        if i % 10 == 3:
            answer += 3600
        else:
            answer += temp_cnt

    return answer


if __name__ == '__main__':
    result = 11475
    solution_result = solution(5)
    print("Success" if result == solution_result else "Fail")
