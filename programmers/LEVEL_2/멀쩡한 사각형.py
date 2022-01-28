def solution(w, h):
    import math
    return w * h - (w + h - math.gcd(w, h))


if __name__ == '__main__':
    result = 20
    w = 3
    h = 11
    solution_result = solution(w, h)
    print("Success" if result == solution_result else "Fail")
