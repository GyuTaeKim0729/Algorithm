def solution(arr):
    arr.remove(min(arr))
    return arr


if __name__ == '__main__':
    result = [4,3,2]
    arr = [4,3,2,1]
    solution_result = solution(arr)
    print("Success" if result == solution_result else "Fail")
