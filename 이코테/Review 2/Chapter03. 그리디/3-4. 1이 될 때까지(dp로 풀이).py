n,k = map(int, input().split())
d = [0]*100001

for i in range(2,n+1):
    d[i] = d[i-1] + 1

    if i % k == 0:
        d[i] = min(d[i], d[i//k]+1)

print(d[n])
