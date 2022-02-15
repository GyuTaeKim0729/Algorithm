can_list = [1]
result_ = [0] * 51


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


def solution2(N, road, K):
    road_map = [[0] * (N + 1) for i in range(N + 1)]
    for i in road:
        if (road_map[i[0]][i[1]] != 0 and road_map[i[0]][i[1]] > i[2]) or road_map[i[0]][i[1]] == 0:
            road_map[i[0]][i[1]] = i[2]
            road_map[i[1]][i[0]] = i[2]

    for i in road_map[1]:
        if i != 0:
            search(N, road_map, K, 0, 1, 0)
    return 51 - result_.count(0) + 1


def search(N, road_map, K, past, now, sum_):
    for i in range(2, N + 1):
        if i != past and road_map[now][i] != 0:
            temp = sum_ + road_map[now][i]
            if (result_[i] == 0 or temp <= result_[i]) and temp <= K:
                result_[i] = temp
                search(N, road_map, K, now, i, temp)


if __name__ == '__main__':
    result = 4
    N, road, K = 5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3
    solution_result = solution2(N, road, K)
    print("Success" if result == solution_result else "Fail")
