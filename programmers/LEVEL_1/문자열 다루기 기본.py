def solution(s):
    if len(s) not in [4, 6]:
        return False

    for i in range(len(s)):
        if ord('0') > ord(s[i]) or ord('9') < ord(s[i]):
            return False
    return True


def solution2(s):
    try:
        int(s)
    except:
        return False
    return len(s) in [4, 6]


if __name__ == '__main__':
    result = False
    s = "a234"
    solution_result = solution(s)
    print("Success" if result == solution_result else "Fail")
