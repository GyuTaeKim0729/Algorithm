def solution(numbers):
    left_numbers = [x for x in range(0, 10)]
    for i in numbers:
        left_numbers.remove(i)
    return sum(left_numbers)


def solution2(numbers):
    return sum(range(10)) - sum(numbers)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 6, 7, 8, 0]
    result = 14
    solution_result = solution2(numbers)
    print("Success" if result == solution_result else "Fail")
