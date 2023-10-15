from itertools import combinations

n,m = map(int, input().split())
data = list(map(int, input().split()))
result = list(combinations(data,2))

cnt = 0
for i in result:
    if i[0] != i[1]:
        cnt += 1

print(cnt)
