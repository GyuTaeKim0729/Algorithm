n = 2
arr = [('홍',95),('리',77)]
temp = sorted(arr, key=lambda x:x[1])
for i in temp:
    print(i[0])