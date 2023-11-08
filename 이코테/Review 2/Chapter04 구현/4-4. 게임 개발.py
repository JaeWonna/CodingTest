n,m = map(int, input().split())
x,y,direction = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

d = [[0]*m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
d[x][y] = 1

def turn_left():
    global direction
    direction = (direction-1)%4

cnt = 1
turn_stack = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if board[nx][ny] == 0 and d[nx][ny] == 0:
        d[nx][ny] = 1
        x,y = nx,ny
        turn_stack = 0
        cnt += 1
        
    else:
        turn_stack += 1
        
    if turn_stack == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if board[nx][ny] == 0:
            x,y = nx,ny
            turn_stack = 0
        else:
            break

print(cnt)
