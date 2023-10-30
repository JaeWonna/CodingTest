# 크루스칼 알고리즘 -> 최소 비용으로 신장 트리 만들기 : 사이클 없으면 합류

# 특정 원소가 속한 집합 찾기 -> 같으면 사이클 발생
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력받기
v,e = map(int, input().split())
parent = [0]*(v+1)

result = 0
edges = []

# 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

for i in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost,a,b = edge

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)

