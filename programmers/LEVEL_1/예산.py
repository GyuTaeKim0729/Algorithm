def solution(d, budget):
    answer = 0
    sum_d = 0
    d.sort()
    for i in d:
        sum_d += i
        if sum_d > budget:
            break
        answer += 1
    return answer


def solution2(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if sum(d) <= budget:
            answer = len(d)
            break
        d.pop()
    return answer


if __name__ == '__main__':
    result = 3
    d = [1, 3, 2, 5, 4]
    budget = 9
    solution_result = solution(d, budget)
    print("Success" if result == solution_result else "Fail")
