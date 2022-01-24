def solution(s):
    answer = ""
    s = s.lower()
    big_flag = True
    for i in s:
        if i == " ":
            big_flag = True
            answer += " "
        else:
            answer += i.upper() if big_flag else i
            big_flag = not big_flag
    return answer


if __name__ == '__main__':
    result = "TrY HeLlO WoRlD"
    s = "tRy hello world"
    solution_result = solution(s)
    print("Success" if result == solution_result else "Fail")
