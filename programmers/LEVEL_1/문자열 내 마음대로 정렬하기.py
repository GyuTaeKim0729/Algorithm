def solution(strings, n):
    strings.sort()
    answer = sorted(strings, key=lambda x: x[n])
    return answer


if __name__ == '__main__':
    result = ["abcd", "abce", "cdx"]
    strings = ["abce", "abcd", "cdx"]
    n = 2
    solution_result = solution(strings, n)
    print("Success" if result == solution_result else "Fail")
