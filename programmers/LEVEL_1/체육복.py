def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = n - len(lost)

    for i in range(1, n + 1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
            answer += 1

    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
            answer += 1
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            answer += 1

    return answer


if __name__ == '__main__':
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]
    result = 5
    solution_result = solution(n, lost, reserve)
    print("Success" if result == solution_result else "Fail")
