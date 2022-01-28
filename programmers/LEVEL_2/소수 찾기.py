def solution(numbers):
    from itertools import permutations
    answer = 0
    find_list = [0, 1]
    num_list = list(numbers)
    for k in range(1, len(num_list) + 1):
        for i in permutations(num_list, k):
            temp = int(''.join(i))
            if temp not in find_list:
                find_list.append(temp)
                if checker(temp):
                    print(temp)
                    answer += 1
    return answer


def checker(num):
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    result = 2
    numbers = "011"
    solution_result = solution(numbers)
    print("Success" if result == solution_result else "Fail")
