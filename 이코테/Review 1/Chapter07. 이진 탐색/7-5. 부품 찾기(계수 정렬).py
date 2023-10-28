n = int(input())
array = list(map(int, input().split()))
count = [0]*(max(array)+1)
for i in range(n):
    count[array[i]] += 1

m = int(input())
data = list(map(int, input().split()))

for i in data:
    if count[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
