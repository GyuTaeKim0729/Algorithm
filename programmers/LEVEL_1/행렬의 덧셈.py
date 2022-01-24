def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[0])):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)
    return answer


def solution2(arr1, arr2):
    return [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]


if __name__ == '__main__':
    result = [[4, 6], [7, 9]]
    arr1 = [[1, 2], [2, 3]]
    arr2 = [[3, 4], [5, 6]]
    solution_result = solution(arr1, arr2)
    print("Success" if result == solution_result else "Fail")
