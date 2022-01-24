def solution(n):
    temp_list = [x for x in range(n+1)]
    for i in range(2, n + 1):
        if temp_list[i] == 0:
            continue
        for j in range(2*i,n+1, i):
            temp_list[j] = 0

    return n - temp_list.count(0)


if __name__ == '__main__':
    result = 4
    n = 10
    solution_result = solution(n)
    print("Success" if result == solution_result else "Fail")
