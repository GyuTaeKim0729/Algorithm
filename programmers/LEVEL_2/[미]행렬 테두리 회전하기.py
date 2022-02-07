def solution(rows, columns, queries):
    answer = []
    box = [[x + (rows*y) + 1 for x in range(rows)] for y in range(columns)]

    

    return answer


if __name__ == '__main__':
    result = [1]
    rows = 100
    columns = 97
    queries = [[1,1,100,97]]
    solution_result = solution(rows, columns, queries)
    print("Success" if result == solution_result else "Fail")
