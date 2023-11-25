n,m = map(int, input().split())
graph = []

for i in range(n):
    data = list(map(int, input()))
    graph.append(data)

def dfs(x,y):
    if x < 0 or y < 0 or x >= n or y >= m: # 범위초과
        return False
    if graph[x][y] == 1: # 장애물
        return False
    if graph[x][y] == 0: # 해당사항
        graph[x][y] = 1 # 방문처리
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)
