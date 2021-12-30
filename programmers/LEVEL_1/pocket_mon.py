def solution(nums):
    max_mon = int(len(nums) / 2)
    temp_set = len(set(nums))
    return temp_set if max_mon > temp_set else max_mon


def solution2(nums):
    return min(len(nums) / 2, len(set(nums)))


if __name__ == '__main__':
    nums = [3, 3, 3, 2, 2, 4]
    result = 3
    solution_result = solution2(nums)
    print("Success" if result == solution_result else "Fail")
