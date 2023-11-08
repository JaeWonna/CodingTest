n = int(input())
directions = list(input().split())
x,y = 1,1
dx = [0,1,0,-1]
dy = [1,0,-1,0]
steps = ['R','D','L','U']

for direction in directions:
    for i in range(4):
        if direction == steps[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx >= 1 and nx <= n and ny >= 1 and ny <= n:
        x,y = nx,ny

print(x,y)
