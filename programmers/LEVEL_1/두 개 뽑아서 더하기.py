def solution(numbers):
    answer = []

    for i in range(len(numbers) - 1):
        for j in numbers[i + 1:]:
            temp_sum = numbers[i] + j
            if temp_sum not in answer:
                answer.append(temp_sum)
    answer.sort()
    return answer


def solution2(numbers):
    answer = []

    from itertools import combinations
    for i in combinations(numbers, 2):
        answer.append(sum(i))
    answer = list(set(answer))
    answer.sort()
    return answer


if __name__ == '__main__':
    result = [2, 3, 4, 5, 6, 7]
    numbers = [2, 1, 3, 4, 1]
    solution_result = solution2(numbers)
    print("Success" if result == solution_result else "Fail")
