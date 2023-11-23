# 플로이드 워셜
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF]*(n+1) for i in range(n+1)]

# 1. 자기 자신은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# 2.각 간선에 대한 정보 입력
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
