from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
apple = [[0]*(n+1) for _ in range(n+1)]
turn_array = []

k = int(input()) # 사과 개수
for i in range(k):
    a,b = map(int, input().split())
    apple[a][b] = 1

m = int(input()) # 변환 횟수
for i in range(m):
    a,b = input().split()
    turn_array.append((int(a), b))

## 생략 ##

def turn_direction(direction, x):
    if x == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


## 생략 ##

# 본문

def solution():
    x,y = 1,1
    direction = 1
    time = 0
    q = deque([(x,y)])

    while True:    
        time += 1
        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx <= 0 or ny <= 0 or nx > n or ny > n: # 벽 밖
            break
        elif (nx,ny) in q: # 자기몸 부딪
            break
        else: # 사과 있 / 없
            if apple[nx][ny] == 1:
                apple[nx][ny] = 0
                q.append((nx,ny))
            else:
                q.popleft()
                q.append((nx,ny))
        
        x,y = nx,ny # 확정 바꿔주고
        
        for i in turn_array:
            if time == i[0]:
                direction = turn_direction(direction, i[1])
    
    return time

print(solution())
