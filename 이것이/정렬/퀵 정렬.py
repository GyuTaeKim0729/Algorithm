arr = [4,2,1,3]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

arr=quick_sort(arr)
print(arr)

arr = [('apple',2),('help',1)]
temp = sorted(arr, key=lambda x:x[1])
print(arr)
print(temp)