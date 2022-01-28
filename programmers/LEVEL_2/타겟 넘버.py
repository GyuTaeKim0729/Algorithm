def solution(numbers, target):
    num_list = [numbers[0], -numbers[0]]

    for i in numbers[1:]:
        temp = []
        for j in num_list:
            temp.append(j + i)
            temp.append(j - i)
        num_list.clear()
        num_list.extend(temp)
    answer = num_list.count(target)
    return answer


def solution2(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    return solution2(numbers[1:], target - numbers[0]) + solution2(numbers[1:], target + numbers[0])


if __name__ == '__main__':
    result = 5
    numbers = [1, 1, 1, 1, 1]
    target = 3
    solution_result = solution2(numbers, target)
    print("Success" if result == solution_result else "Fail")
