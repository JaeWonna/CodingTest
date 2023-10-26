from collections import deque

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 상하좌우 개념 + bfs 큐 개념
def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft() # (큐)popleft 빼기

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 그래프 범위밖
                continue
            if graph[nx][ny] == 0: # 괴물이 있는 부분
                continue
            if graph[nx][ny] == 1: # 괴물이 없는 부분 + 처음 가는 부분
                graph[nx][ny] = graph[x][y] + 1 # visited 대신
                queue.append((nx,ny)) # (큐)apppend 추가
    return graph[n-1][m-1]        
    
print(bfs(0,0))




