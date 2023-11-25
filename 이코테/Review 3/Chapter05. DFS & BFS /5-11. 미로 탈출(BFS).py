from collections import deque

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 범위밖
                continue
            if graph[nx][ny] == 0: # 장애물
                continue
            if graph[nx][ny] == 1: # 해당경우
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
    
    return graph[n-1][m-1]

print(bfs(0,0))
