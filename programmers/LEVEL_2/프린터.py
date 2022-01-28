def solution(priorities, location):
    answer = 0
    temp_location = location
    max_value = max(priorities)
    while True:
        if max_value == priorities[0]:
            priorities.pop(0)
            answer += 1
            if temp_location == 0:
                return answer
            max_value = max(priorities)
        else:
            temp = priorities.pop(0)
            priorities.append(temp)
            if temp_location == 0:
                temp_location = len(priorities)
        temp_location -= 1


if __name__ == '__main__':
    result = 1
    priorities = [2, 1, 3, 2]
    location = 2
    solution_result = solution(priorities, location)
    print("Success" if result == solution_result else "Fail")
