can_list = [1]


def solution(N, road, K):



    research(N, road, K, 1, 0, 0, 0)
    return len(can_list)


def research(N, road, K, now, past, sum_, turn_cnt):
    if sum_ <= K and turn_cnt < N:
        for i in road:
            if i[0] != past and i[1] != past and (i[0] == now or i[1] == now):
                temp_sum = sum_ + i[2]
                if i[0] == now and temp_sum <= K:
                    if i[1] not in can_list:
                        can_list.append(i[1])

                    research(N, road, K, i[1], now, temp_sum, turn_cnt + 1)
                elif i[1] == now and temp_sum <= K:
                    if i[0] not in can_list:
                        can_list.append(i[0])
                    research(N, road, K, i[0], now, temp_sum, turn_cnt + 1)


if __name__ == '__main__':
    result = 4
    N, road, K = 5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3
    solution_result = solution(N, road, K)
    print("Success" if result == solution_result else "Fail")
