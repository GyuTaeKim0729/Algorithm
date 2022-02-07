def solution(name):
    answer = 0
    temp_name = ['A' for i in range(len(name))]
    now = 0

    while temp_name.count('A') != name.count('A'):
        go_cnt = find_a(name, temp_name, True, now)
        back_cnt = find_a(name, temp_name, False, now)

        if go_cnt <= back_cnt:
            now = (now + go_cnt) % len(name)
            answer += go_cnt
        else:
            now = (now - back_cnt) % len(name)
            answer += back_cnt
        print(temp_name, now)
        temp_name[now] = name[now]

    for i in name:
        if ord(i) > ord('N'):
            answer += ord('Z') - ord(i) + 1
        else:
            answer += ord(i) - ord('A')

    return answer


def find_a(name, name_in, go_back, now):
    count = 0
    while True:
        if name[(now + count) % len(name)] != name_in[(now + count) % len(name)]:
            return abs(count)
        if go_back:
            count += 1
        else:
            count -= 1


if __name__ == '__main__':
    result = 7 + 4
    name = "AABAAAAAAABBB"
    solution_result = solution(name)
    print(solution_result)
    print("Success" if result == solution_result else "Fail")
