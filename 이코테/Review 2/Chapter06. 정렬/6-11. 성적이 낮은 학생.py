n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    data.append((name, int(score)))

result = sorted(data, key = lambda x : x[1])

for i in result:
    print(i[0], end=' ')
