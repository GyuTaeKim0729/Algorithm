n = 4
m = 6
arr = [19, 15, 10, 17]

def sum_d(arr,h):
    sum_val = 0
    for i in arr:
        if i > h:
            sum_val += (i-h)
    return sum_val



start = 0
end = max(arr)
mid = 0

while start <= end:
    mid = (start + end) // 2
    d_val = sum_d(arr,mid)
    if d_val == m:
        break
    # 떡이 기준 보다 작을 경우
    elif d_val < m:
        end = mid - 1
    # 떡이 기준 보다 클 경우
    else:
        start = mid + 1

print(mid)
