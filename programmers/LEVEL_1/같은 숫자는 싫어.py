def solution(arr):
    answer = []
    before = -1
    for i in arr:
        if i != before:
            answer.append(i)
        before = i
    return answer


if __name__ == '__main__':
    result = [4,3]
    arr = [4,4,4,3,3]
    solution_result = solution(arr)
    print("Success" if result == solution_result else "Fail")
