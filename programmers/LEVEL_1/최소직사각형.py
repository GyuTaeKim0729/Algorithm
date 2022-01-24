def solution(sizes):
    from functools import reduce
    answer_size = [0, 0]

    for i in sizes:
        i.sort()
        if answer_size[0] < i[0]:
            answer_size[0] = i[0]

        if answer_size[1] < i[1]:
            answer_size[1] = i[1]
    answer = reduce(lambda x, y: x * y, answer_size)
    return answer


def solution2(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes) # 큰 거 중에 가장 큰거, 작은 거 중에 가장 큰거


if __name__ == '__main__':
    sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
    result = 4000
    solution_result = solution2(sizes)
    print("Success" if result == solution_result else "Fail")
