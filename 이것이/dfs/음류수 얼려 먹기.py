def solution(tt):
    answer = 0
    steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x in range(len(tt)):
        for y in range(len(tt[0])):
            if tt[x][y] == 0:
                answer += 1
                stack = [(x, y)]
                while stack:
                    temp = stack.pop()
                    nx = temp[0]
                    ny = temp[1]
                    for i in steps:
                        temp_x = nx + i[0]
                        temp_y = ny + i[1]
                        if 0 <= temp_x < len(tt) and 0 <= temp_y < len(tt[0]) and tt[temp_x][temp_y] == 0:
                            tt[temp_x][temp_y] = 2
                            stack.append((temp_x, temp_y))
    print(answer)
    return answer


if __name__ == '__main__':
    result = 0
    solution_result = solution([[0, 0, 1], [0,1,0], [1, 0, 1]])
    print("Success" if result == solution_result else "Fail")
