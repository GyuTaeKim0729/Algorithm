def solution(arr, divisor):
    answer = [-1]
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) != 1:
        answer.pop(0)
    answer.sort()
    return answer


def solution2(arr, divisor):
    answer = sorted([x for x in arr if x % divisor == 0]) or [-1]
    return answer


if __name__ == '__main__':
    result = [5, 10]
    arr = [5, 9, 7, 10]
    divisor = 5
    solution_result = solution2(arr, divisor)
    print("Success" if result == solution_result else "Fail")
