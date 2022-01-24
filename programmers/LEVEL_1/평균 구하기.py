def solution(arr):
    return sum(arr)/len(arr)


if __name__ == '__main__':
    result = 2.5
    arr = [1,2,3,4]
    solution_result = solution(arr)
    print("Success" if result == solution_result else "Fail")
