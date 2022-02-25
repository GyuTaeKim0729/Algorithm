N,M,K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
answer = 0
cnt = 0
for _ in range(M):
    if cnt == K:
        answer += data[-2]
        cnt = 0
    else:
        answer += data[-1]
        cnt += 1

while True:
    for i in range(K):
        if M == 0:
            break
        M -= 1
        answer += data[-1]
    if M == 0:
        break
    answer += data[-2]
    M -= 1

temp = 0
count = K * M//(K+1) * K  # 큰수 반복 횟수 4 4 4 3 에서는 4는 3회!
count += M % (K+1)  # 나머지 큰수 횟수
answer += data[-1] * count
answer += data[-2] * (M-count)

print(answer)