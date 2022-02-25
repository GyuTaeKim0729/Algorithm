def solution(N, K):
    answer = 0
    while N != 1:
        if N % K == 0:
            N //= K
        else:
            N -= 1
        answer += 1

    return answer

def solu2(N, K):
    answer = 0
    while True:
        temp = (N // K) * K
        answer += (N - temp)
        N = temp
        if N < K:
            break
        N = N//K
        answer += 1

    return answer + (N - 1)

if __name__ == '__main__':
    result = 6
    solution_result = solu2(25, 3)
    print("Success" if result == solution_result else "Fail")
