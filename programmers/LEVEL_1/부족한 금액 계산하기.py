def solution(price, money, count):
    for i in range(1, count + 1):
        money -= price * i
    answer = abs(money)
    if money > 0:
        answer = 0
    return answer


def solution2(price, money, count):
    temp_price = sum([price * i for i in range(1, count + 1)])
    if temp_price > money:
        return temp_price - money
    return 0


if __name__ == '__main__':
    result = 10
    price = 3
    money = 20
    count = 4
    solution_result = solution2(price, money, count)
    print("Success" if result == solution_result else "Fail")
