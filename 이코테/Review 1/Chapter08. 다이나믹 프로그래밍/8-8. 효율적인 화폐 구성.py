n,m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
array.sort()

# 인덱스 값을 만들기 위해 필요한 동전의 개수 -> 최소값
INF = int(1e9)
d = [INF]*(m+1)
d[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != INF:
            d[j] = min(d[j], d[j-array[i]]+1) # 동전사용

if d[m] == INF:
    print(-1)
else:
    print(d[m])
