from itertools import combinations

n,m = map(int, input().split())
data = list(map(int, input().split()))

result = list(combinations(data,2))

cnt = 0
for a,b in result:
    if a != b:
        cnt += 1

print(cnt)
