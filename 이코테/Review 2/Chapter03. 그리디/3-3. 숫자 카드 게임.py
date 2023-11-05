n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

result = 0

for i in range(n):
    min_value = min(graph[i])
    result = max(result, min_value)

print(result)
