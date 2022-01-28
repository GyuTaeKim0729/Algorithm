def solution(scoville, K):
    import heapq

    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        min_1 = heapq.heappop(scoville)
        min_2 = heapq.heappop(scoville)

        if min_1 >= K:
            break

        temp = min_1 + min_2 * 2
        heapq.heappush(scoville, temp)
        answer += 1

    if len(scoville) == 1 and scoville[0] < K:
        answer = -1

    return answer


if __name__ == '__main__':
    result = 2
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    solution_result = solution(scoville, K)
    print("Success" if result == solution_result else "Fail")
