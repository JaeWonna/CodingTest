# 같은 집합에 속해있는지 확인. 같은값일시 사이클
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 팁 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().split())
parent = [0]*(v+1)

for i in range(1,v+1):
    parent[i] = i

for i in range(e):
    x,a,b = map(int, input().split())

    if x == 0:
        union_parent(parent,a,b)
    elif x == 1:
        if find_parent(parent,a) == find_parent(parent,b):
            print('YES')
        else:
            print('NO')
