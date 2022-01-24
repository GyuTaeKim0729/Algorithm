def solution(s, n):
    answer = ''
    for i in s:
        if i != ' ':
            if ord(i) >= ord('a'):
                if ord(i) + n > ord('z'):
                    answer += chr(ord(i) + n - ord('z') + ord('a') - 1)
                else:
                    answer += chr(ord(i) + n)
            else:
                if ord(i) + n > ord('Z'):
                    answer += chr(ord(i) + n - ord('Z') + ord('A') - 1)
                else:
                    answer += chr(ord(i) + n)
        else:
            answer += i
    return answer


def solution2(s, n):
    answer = ''
    for i in s:
        if i != ' ':
            if ord(i) >= ord('a'):
                answer += chr(((ord(i) + n - ord('a')) % 26) + ord('a'))
            else:
                answer += chr(((ord(i) + n - ord('A')) % 26) + ord('A'))
        else:
            answer += i
    return answer


if __name__ == '__main__':
    result = "a"
    s = "z"
    n = 1
    solution_result = solution2(s, n)
    print("Success" if result == solution_result else "Fail")
