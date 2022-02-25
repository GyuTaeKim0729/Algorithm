arr = [1,2,5,4,3]
brr = [5,5,6,6,5]
n = 5
k = 3

arr.sort()
brr.sort(reverse=True)

for i in range(3):
    if arr[i] < brr[i]:
        arr[i], brr[i] = brr[i], arr[i]
    else:
        break

print(arr, brr)
print(sum(arr))