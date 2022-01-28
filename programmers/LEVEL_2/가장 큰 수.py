import functools


def cmp(a, b):
    if a + b > b + a:
        return 1
    elif a + b == b + a:
        return 0
    else:
        return -1


def solution(numbers):
    temp_num = [str(i) for i in numbers]
    temp_num = sorted(temp_num, key=functools.cmp_to_key(cmp), reverse=True)
    answer = ''.join(temp_num)
    if int(answer) == 0:
        answer = '0'
    return answer


if __name__ == '__main__':
    result = "0"
    numbers = [0,0,0]
    solution_result = solution(numbers)
    print("Success" if result == solution_result else "Fail")
