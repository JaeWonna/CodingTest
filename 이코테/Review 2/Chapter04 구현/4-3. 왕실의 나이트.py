data = list(input())
x = int(data[1])
y = int(ord(data[0])) - int(ord('a')) + 1
steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
cnt = 0

for step in steps:
    nx = x + step[0]
    ny = y + step[1]

    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        cnt += 1

print(cnt)
