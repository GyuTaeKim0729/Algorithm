def solution(input_):
    a, b = map(int, input_.strip().split(' '))
    for i in range(b):
        print('*'*a)
    return 0


if __name__ == '__main__':
    result = 0
    input_ = '5 3'
    solution_result = solution(input_)
    print("Success" if result == solution_result else "Fail")
