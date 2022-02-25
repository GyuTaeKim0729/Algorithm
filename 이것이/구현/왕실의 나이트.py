def solution(nums):
    answer = 0
    steps = [(-2,1),(-2,-1),(-1,2),(-1,-2),(1,2),(1,-2),(2,-1),(2,1)]
    x = ord(nums[0]) - ord('a') + 1
    y = int(nums[1])
    for i in steps:
        temp_x = x + i[0]
        temp_y = y + i[1]
        if 0 < temp_x < 9 and 0 < temp_y < 9:
            answer += 1

    return answer


if __name__ == '__main__':
    result = 6
    solution_result = solution('c2')
    print("Success" if result == solution_result else "Fail")
