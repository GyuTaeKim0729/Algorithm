from collections import deque


def solution(n, m, mapp):
    answer = 0
    visited = []
    queue = deque([(0, 0)])
    steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        temp = queue.popleft()
        if temp not in visited:
            visited.append(temp)
            x = temp[0]
            y = temp[1]
            for i in steps:
                nx = x + i[0]
                ny = y + i[1]
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and mapp[nx][ny] == 1:
                    mapp[nx][ny] = mapp[x][y] + 1
                    queue.append((nx, ny))
    print(mapp[n-1][m-1])
    return answer


if __name__ == '__main__':
    result = 0
    solution_result = solution(5, 6, [[1,0, 1, 0,1,0], [1,1,1,1,1,1], [0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]])
    print("Success" if result == solution_result else "Fail")
