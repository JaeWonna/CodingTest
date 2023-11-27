# 서로소 집합 알고리즘
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
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

edges = []
result = 0

for i in range(1,v+1):
    parent[i] = i

for i in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))

edges.sort() # 연결하되 cost가 작은 값부터 정렬
last = 0

for edge in edges: # 작은 값부터 하나씩 꺼내기
    cost,a,b = edge

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        last = cost

print(result - last)

