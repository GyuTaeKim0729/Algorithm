def solution(phone_number):
    answer = ''
    for k in range(len(phone_number) - 4):
        answer += '*'
    return answer + phone_number[len(phone_number) - 4:]


def solution2(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]


if __name__ == '__main__':
    result = "*******4444"
    phone_number = "01033334444"
    solution_result = solution2(phone_number)
    print("Success" if result == solution_result else "Fail")
