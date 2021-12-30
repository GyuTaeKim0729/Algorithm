def solution(n):
    answer = 0
    reversed_temp = []
    temp_n = n
    max_cnt = 0
    while int(temp_n / 3) != 0:
        temp_n = temp_n / 3
        max_cnt += 1

    left = n
    for i in reversed(range(max_cnt + 1)):
        if left >= 2 * (3 ** i):
            left = left - 2 * (3 ** i)
            reversed_temp.append(2)
        elif left >= (3 ** i):
            left = left - (3 ** i)
            reversed_temp.append(1)
        else:
            reversed_temp.append(0)

    for index, value in enumerate(reversed_temp):
        answer += value * (3 ** index)
    return answer


def solution2(n):
    temp = ''
    temp_n = n
    while temp_n:
        temp += str(temp_n % 3)
        temp_n = temp_n // 3
    return int(temp, 3)


if __name__ == '__main__':
    n = 125
    result = 229
    solution_result = solution2(n)
    print("Success" if result == solution_result else "Fail")
