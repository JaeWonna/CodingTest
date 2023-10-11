import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

# 그래프 정보 입력
for i in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

# 다익스트라 정의
def dijkstra(start):
    q = []

    heapq.heappush(q, (0,start)) # dist, now
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist: # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 수행
dijkstra(start)

# 결과 출력
cnt = 0
find_max = 0

for d in distance: # 인덱스 0이 INF인것까지 포함됨
    if d != INF:
        cnt += 1
        find_max = max(find_max, d)

print(cnt-1, find_max)
