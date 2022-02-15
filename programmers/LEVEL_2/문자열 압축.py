def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):  # 1개부터 짜른다.
        now_temp = ''
        now_cnt = 0
        temp_answer = len(s)
        for j in range(0,len(s),i):
            if s[j:j+i] == s[j+i:j+i+i]:
                if now_temp == s[j:j+i]:
                    temp_answer -= i
                    now_cnt += 1
                    if now_cnt == 8:
                        temp_answer += 1
                else:
                    now_temp = s[j:j+i]
                    temp_answer -= i
                    temp_answer += 1
            else:
                now_temp = ''
                now_cnt = 0
        answer = temp_answer if temp_answer < answer else answer
    return answer


if __name__ == '__main__':
    result = 5
    s = "xxxxxxxxxxyyy"  # abr 2abc adq 2abc
    solution_result = solution(s)
    print("Success" if result == solution_result else "Fail")
