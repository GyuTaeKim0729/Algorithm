def solution(nums):
    answer = 0
    length_nums = len(nums)
    for i in range(length_nums - 2):
        for j in range(i + 1, length_nums - 1):
            for k in range(j + 1, length_nums):
                temp_sum = nums[i] + nums[j] + nums[k]
                for v in range(2, temp_sum - 1):
                    if temp_sum % v == 0:
                        temp_sum = 0
                        break
                if temp_sum != 0:
                    answer += 1

    return answer


"""
from itertools import combinations
list에서 r-길이 튜플들, 정리된 순서, 반복되는 요소 없음
https://docs.python.org/ko/3/library/itertools.html
해당 링크는 공부가 필요한 것으로 보임.

* for-else
for문이 break되지 않고 끝까지 완수할 경우
else문을 실행하도록 한다.
"""


def solution2(nums):
    from itertools import combinations
    answer = 0
    for i in combinations(nums, 3):
        temp_sum = sum(i)
        for j in range(2, temp_sum):
            if temp_sum % j == 0:
                break
        else:
            answer += 1
    return answer


if __name__ == '__main__':
    nums = [1, 2, 7, 6, 4]
    result = 4
    solution_result = solution2(nums)
    print(solution_result)
    print("Success" if result == solution_result else "Fail")
