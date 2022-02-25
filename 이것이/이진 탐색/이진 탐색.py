arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


def binary_search(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return binary_search(arr, target, start, mid - 1)


result = binary_search(arr, 7, 0, len(arr))
print(result + 1)

start = 0
end = len(arr)
target = 7
mid = 0
while start <= end:
    mid = (start+end)//2
    if arr[mid] == target:
        break
    elif arr[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
print(mid+1)