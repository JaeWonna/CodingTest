MAX = int(1e9)
n,m = map(int, input().split())
d = [MAX]*(m+1)
d[0] = 0
coins = []

for i in range(n):
    coins.append(int(input()))

for i in range(n):
    for j in range(coins[i], m+1):
        if d[j-coins[i]] != MAX:
            d[j] = min(d[j], d[j-coins[i]]+1)

if d[m] == MAX:
    print(-1)
else:
    print(d[m])
