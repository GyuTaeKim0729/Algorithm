n = 5
arr = [8,3,7,9,2]
m = 3
brr = [5, 7, 9]

answer = []

for i in brr:
    if i in arr:
        answer.append('yes')
    else:
        answer.append('No')

temp = ' '.join(answer)
print(temp)

answer2 = []

mid = 0
arr.sort()
brr.sort()

for i in brr:
    start = 0
    end = len(arr)
    while start <= end:
        mid = (start+end)//2

        if arr[mid] == i:
            answer2.append('Yes')
            break
        elif arr[mid] < i:
            start = mid + 1
        else:
            end = mid - 1

    if start >= end:
        answer2.append('No')

print(' '.join(answer2))