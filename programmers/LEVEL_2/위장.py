def solution(clothes):
    answer = 1
    clothes_set = {}
    for i in clothes:
        if i[1] not in clothes_set:
            clothes_set[i[1]] = [i[0]]
        else:
            clothes_set[i[1]].append(i[0])

    for i in clothes_set:
        answer *= (len(clothes_set[i]) + 1)
    return answer - 1


if __name__ == '__main__':
    result = 3
    clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    solution_result = solution(clothes)
    print("Success" if result == solution_result else "Fail")
