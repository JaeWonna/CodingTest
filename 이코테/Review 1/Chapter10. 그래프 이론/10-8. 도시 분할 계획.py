def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().split())
parent = [0]*(v+1)
result = 0
edges = []

for i in range(1,v+1):
    parent[i] = i

for i in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))

edges.sort()
last = 0

# 간선을 하나씩 확인하며 최소 비용 순서로 사이클 발생 x시 비용계산
for edge in edges:
    cost,a,b = edge

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        last = cost

print(result - last)

