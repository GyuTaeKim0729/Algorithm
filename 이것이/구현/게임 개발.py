def solution(N, M, now, direct, maps):
    answer = 0
    x = now[0]
    y = now[1]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    maps[now[0]][now[1]] = 2
    answer += 1
    turn_cnt = 0
    while True:
        # 가보지 않은 칸
        direct = direct_set(direct)
        nx = x+dx[direct]
        ny = y+dx[direct]

        if maps[nx][ny] == 0:
            x, y = nx, ny
            answer += 1
            maps[x][y] = 2
            turn_cnt = 0
        else:
            turn_cnt += 1
        if turn_cnt == 4:
            nx = x-dx[direct]
            ny = x-dy[direct]
            if maps[nx][ny] == 1:
                break
            else:
                x, y = nx, ny
                turn_cnt = 0
    return answer


def direct_set(direct):
    temp = direct - 1
    if temp < 0:
        temp = 3
    return temp


if __name__ == '__main__':
    result = 3
    N, M = 4, 4
    now = [1, 1]
    direct = 0
    maps = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
    solution_result = solution(N, M, now, direct, maps)
    print("Success" if result == solution_result else "Fail")
